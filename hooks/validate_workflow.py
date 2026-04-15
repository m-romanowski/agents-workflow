#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


REQUIRED_TOP_LEVEL_FILES = [
    "AGENTS.md",
    "BOOTSTRAP.md",
    "README.md",
    "instructions/core/session-contract.md",
    "instructions/work/README.md",
]

CRITICAL_REFERENCES = {
    "README.md": {
        ".gitignore": "link",
        "instructions/core/workflow-mode-matrix.md": "link",
    },
    "BOOTSTRAP.md": {
        "AGENTS.md": "path",
        "instructions/core/session-contract.md": "path",
        "instructions/project/index.md": "path",
    },
}

REQUIRED_FRONT_MATTER_KEYS = {
    "task_id",
    "title",
    "status",
    "mode",
    "tracking",
    "current_phase",
    "current_step",
    "current_milestone",
    "step_status",
    "approved_steps",
    "latest_checkpoint",
    "resume_from",
    "allowed_paths",
    "requires_operator_approval",
    "last_updated",
}

ALLOWED_STATUS = {"draft", "active", "blocked", "completed"}
ALLOWED_MODE = {"plan", "implement"}
ALLOWED_TRACKING = {"track"}


@dataclass
class Finding:
    level: str
    path: str
    message: str


class FrontMatterError(Exception):
    pass


def extract_front_matter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None

    closing_index = text.find("\n---\n", 4)
    if closing_index == -1:
        if text.endswith("\n---"):
            closing_index = len(text) - 4
        else:
            raise FrontMatterError("front matter is missing a closing --- line")

    return text[4:closing_index]


def parse_scalar(raw: str):
    value = raw.strip()
    if value == "null":
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_nested_block(lines: list[str]):
    meaningful = [line for line in lines if line.strip()]
    if not meaningful:
        return []

    stripped = [line[2:] if line.startswith("  ") else line for line in meaningful]
    if all(line.startswith("- ") for line in stripped):
        return [parse_scalar(line[2:]) for line in stripped]

    result = {}
    for line in stripped:
        if line.startswith(" "):
            raise FrontMatterError(f"unsupported nested indentation: {line!r}")
        if ":" not in line:
            raise FrontMatterError(f"invalid mapping entry: {line!r}")
        key, raw_value = line.split(":", 1)
        result[key.strip()] = parse_scalar(raw_value)
    return result


def parse_front_matter(block: str) -> dict:
    lines = block.splitlines()
    parsed = {}
    index = 0

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith(" "):
            raise FrontMatterError(f"unexpected indentation at top level: {line!r}")
        if ":" not in line:
            raise FrontMatterError(f"invalid top-level entry: {line!r}")

        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()

        if value:
            parsed[key] = parse_scalar(value)
            index += 1
            continue

        nested_lines = []
        index += 1
        while index < len(lines):
            nested = lines[index]
            if nested and not nested.startswith(" "):
                break
            nested_lines.append(nested)
            index += 1
        parsed[key] = parse_nested_block(nested_lines)

    return parsed


def repo_relative(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def add_finding(findings: list[Finding], level: str, path: str, message: str) -> None:
    findings.append(Finding(level=level, path=path, message=message))


def validate_required_files(root: Path, findings: list[Finding]) -> None:
    for relative_path in REQUIRED_TOP_LEVEL_FILES:
        if not (root / relative_path).exists():
            add_finding(findings, "ERROR", relative_path, "required file is missing")


def validate_critical_links(root: Path, findings: list[Finding]) -> None:
    for source_path, targets in CRITICAL_REFERENCES.items():
        source = root / source_path
        if not source.exists():
            continue

        text = source.read_text(encoding="utf-8")
        for target, reference_type in targets.items():
            if reference_type == "link":
                needle = f"]({target})"
            else:
                needle = f"`{target}`"

            if needle not in text:
                add_finding(
                    findings,
                    "ERROR",
                    source_path,
                    f"critical {reference_type} reference is missing: {target}",
                )
                continue
            if not (root / target).exists():
                add_finding(
                    findings,
                    "ERROR",
                    source_path,
                    f"critical link target is missing: {target}",
                )


def validate_todo_front_matter(todo_path: Path, root: Path, findings: list[Finding]) -> None:
    relative_path = repo_relative(todo_path, root)
    text = todo_path.read_text(encoding="utf-8")

    try:
        block = extract_front_matter(text)
    except FrontMatterError as exc:
        add_finding(findings, "ERROR", relative_path, str(exc))
        return

    if block is None:
        add_finding(findings, "ERROR", relative_path, "missing YAML front matter")
        return

    try:
        front_matter = parse_front_matter(block)
    except FrontMatterError as exc:
        add_finding(findings, "ERROR", relative_path, f"invalid front matter: {exc}")
        return

    missing_keys = sorted(REQUIRED_FRONT_MATTER_KEYS - set(front_matter))
    if missing_keys:
        add_finding(
            findings,
            "ERROR",
            relative_path,
            f"missing required front matter keys: {', '.join(missing_keys)}",
        )
        return

    validate_front_matter_types(relative_path, front_matter, findings)
    validate_front_matter_logic(todo_path, relative_path, root, front_matter, findings)


def validate_front_matter_types(relative_path: str, front_matter: dict, findings: list[Finding]) -> None:
    status = front_matter["status"]
    mode = front_matter["mode"]
    tracking = front_matter["tracking"]

    if status not in ALLOWED_STATUS:
        add_finding(findings, "ERROR", relative_path, f"invalid status: {status}")
    if mode not in ALLOWED_MODE:
        add_finding(findings, "ERROR", relative_path, f"invalid mode: {mode}")
    if tracking not in ALLOWED_TRACKING:
        add_finding(findings, "ERROR", relative_path, f"invalid tracking value: {tracking}")

    if not isinstance(front_matter["step_status"], dict):
        add_finding(findings, "ERROR", relative_path, "step_status must be a mapping")
    if not isinstance(front_matter["approved_steps"], list):
        add_finding(findings, "ERROR", relative_path, "approved_steps must be a list")
    if not isinstance(front_matter["allowed_paths"], list):
        add_finding(findings, "ERROR", relative_path, "allowed_paths must be a list")
    if not isinstance(front_matter["requires_operator_approval"], list):
        add_finding(findings, "ERROR", relative_path, "requires_operator_approval must be a list")


def validate_front_matter_logic(
    todo_path: Path,
    relative_path: str,
    root: Path,
    front_matter: dict,
    findings: list[Finding],
) -> None:
    status = front_matter["status"]
    current_step = front_matter["current_step"]
    resume_from = front_matter["resume_from"]
    approved_steps = front_matter["approved_steps"]
    step_status = front_matter["step_status"]

    if status == "completed":
        if current_step is not None:
            add_finding(findings, "ERROR", relative_path, "completed task must have current_step: null")
        if resume_from is not None:
            add_finding(findings, "ERROR", relative_path, "completed task must have resume_from: null")
    else:
        if current_step is None:
            add_finding(findings, "ERROR", relative_path, "active task must declare current_step")
        if resume_from is None:
            add_finding(findings, "ERROR", relative_path, "active task must declare resume_from")

    if current_step is not None:
        if not isinstance(approved_steps, list) or current_step not in approved_steps:
            add_finding(findings, "ERROR", relative_path, "current_step must be listed in approved_steps")
        if not isinstance(step_status, dict) or current_step not in step_status:
            add_finding(findings, "ERROR", relative_path, "current_step must exist in step_status")

    latest_checkpoint = front_matter["latest_checkpoint"]
    if latest_checkpoint is not None:
        checkpoint_path = todo_path.parent / str(latest_checkpoint)
        if not checkpoint_path.exists():
            add_finding(
                findings,
                "ERROR",
                relative_path,
                f"latest_checkpoint points to missing file: {latest_checkpoint}",
            )

    allowed_paths = front_matter["allowed_paths"]
    if isinstance(allowed_paths, list):
        for allowed_path in allowed_paths:
            if not isinstance(allowed_path, str):
                add_finding(findings, "ERROR", relative_path, "allowed_paths entries must be strings")
                continue
            if not (root / allowed_path).exists():
                add_finding(
                    findings,
                    "ERROR",
                    relative_path,
                    f"allowed_paths points to missing path: {allowed_path}",
                )


def collect_todo_files(root: Path) -> list[Path]:
    work_root = root / "instructions/work"
    if not work_root.exists():
        return []
    return sorted(path for path in work_root.glob("*/TODO.md") if path.is_file())


def print_findings(findings: list[Finding]) -> None:
    for finding in findings:
        print(f"{finding.level:<5} {finding.path}  {finding.message}")

    errors = sum(1 for finding in findings if finding.level == "ERROR")
    warnings = sum(1 for finding in findings if finding.level == "WARN")
    print(f"SUMMARY {errors} errors, {warnings} warnings")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    findings: list[Finding] = []

    validate_required_files(root, findings)
    validate_critical_links(root, findings)

    for todo_path in collect_todo_files(root):
        validate_todo_front_matter(todo_path, root, findings)

    print_findings(findings)
    return 1 if any(finding.level == "ERROR" for finding in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
