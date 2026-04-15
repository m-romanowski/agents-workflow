#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

from validate_workflow import extract_front_matter, parse_front_matter


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def list_active_tasks(root: Path) -> list[tuple[Path, dict]]:
    tasks = []
    for todo_path in sorted((root / "instructions/work").glob("*/TODO.md")):
        text = todo_path.read_text(encoding="utf-8")
        block = extract_front_matter(text)
        if block is None:
            continue
        front_matter = parse_front_matter(block)
        if front_matter.get("status") == "active":
            tasks.append((todo_path, front_matter))
    return tasks


def list_completed_tasks(root: Path) -> list[tuple[Path, dict]]:
    tasks = []
    for todo_path in sorted((root / "instructions/work").glob("*/TODO.md")):
        text = todo_path.read_text(encoding="utf-8")
        block = extract_front_matter(text)
        if block is None:
            continue
        front_matter = parse_front_matter(block)
        if front_matter.get("status") == "completed":
            tasks.append((todo_path, front_matter))
    return tasks


def staged_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def is_allowed(path: str, allowed_paths: list[str]) -> bool:
    for allowed in allowed_paths:
        normalized = allowed.rstrip("/")
        if path == normalized:
            return True
        if allowed.endswith("/") and path.startswith(normalized + "/"):
            return True
    return False


def task_prefix(todo_path: Path, root: Path) -> str:
    return str(todo_path.parent.relative_to(root)).rstrip("/") + "/"


def is_task_file(path: str, task_dir_prefix: str) -> bool:
    return path.startswith(task_dir_prefix)


def is_checkpoint_file(path: str, task_dir_prefix: str) -> bool:
    if not is_task_file(path, task_dir_prefix):
        return False
    name = Path(path).name
    return name.startswith("checkpoint-") and name.endswith(".md")


def main() -> int:
    root = repo_root()
    active_tasks = list_active_tasks(root)

    if not active_tasks:
        completed_tasks = list_completed_tasks(root)
        if not completed_tasks:
            return fail("Commit blocked: no active tracked task found under instructions/work/.")
        todo_path, front_matter = completed_tasks[-1]
        task_name = todo_path.parent.name
        if front_matter.get("latest_checkpoint") is None:
            return fail(
                f"Commit blocked: latest completed task {task_name} has no latest_checkpoint for commit authorization."
            )
    elif len(active_tasks) > 1:
        task_names = ", ".join(str(path.parent.name) for path, _ in active_tasks)
        return fail(f"Commit blocked: multiple active tracked tasks found: {task_names}")
    else:
        todo_path, front_matter = active_tasks[0]
        task_name = todo_path.parent.name

        if front_matter.get("mode") != "implement":
            return fail(f"Commit blocked: active task {task_name} is not in implement mode.")
        if front_matter.get("current_step") is None:
            return fail(f"Commit blocked: active task {task_name} has no current_step.")

    allowed_paths = front_matter.get("allowed_paths")
    if not isinstance(allowed_paths, list):
        return fail(f"Commit blocked: active task {task_name} has invalid allowed_paths.")

    staged = staged_files(root)
    disallowed = [path for path in staged if not is_allowed(path, allowed_paths)]
    if disallowed:
        print(f"Commit blocked: staged files are outside allowed_paths for {task_name}:", file=sys.stderr)
        for path in disallowed:
            print(f"- {path}", file=sys.stderr)
        return 1

    task_dir_prefix = task_prefix(todo_path, root)
    external_changes = [path for path in staged if not is_task_file(path, task_dir_prefix)]
    checkpoint_changes = [path for path in staged if is_checkpoint_file(path, task_dir_prefix)]

    if external_changes and not checkpoint_changes and front_matter.get("status") != "completed":
        print(
            f"Commit blocked: staged files outside {task_name} require a staged checkpoint file in the active task:",
            file=sys.stderr,
        )
        for path in external_changes:
            print(f"- {path}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
