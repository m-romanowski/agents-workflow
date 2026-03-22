# Spock Examples

## Purpose

- optional cold-loaded examples showing the backend-testing strategy in Spock-style syntax

## Use This File When

- the task needs concrete Spock examples for behaviour-focused tests
- the task involves translating the generic testing strategy into Spock structure

## Example: Behaviour At A Module API Boundary

```groovy
class OrderFacadeSpec extends Specification implements SampleOrders {
    OrderFacade facade = new OrderConfiguration().orderFacade()

    def "should register a pending order and return approval link"() {
        when: "customer places a valid order"
            ApprovalLinkDto result = facade.newOrder(validOrder)

        then: "system returns the approval link"
            result.value() == "https://payments.test/approval/payment-1"
    }

    def "should reject empty order"() {
        when: "customer tries to place an empty order"
            facade.newOrder(emptyOrder)

        then:
            thrown(IllegalOrderStateException)
    }
}
```

Use this shape when:

- the module can be created through a public configuration entry such as `new OrderConfiguration().orderFacade()`
- test collaborators can be supplied through configuration when needed without exposing internal service wiring
- assertions stay on observable behaviour exposed by the facade

## Example: Shared Sample Data Helper

```groovy
@CompileStatic
trait SampleOrders {
    OrderDto validOrder = new OrderDto(
            "user-1",
            [new OrderDto.ProductDto(UUID.fromString("11111111-1111-1111-1111-111111111111"), 2)] as Set
    )
    OrderDto emptyOrder = new OrderDto("user-1", [] as Set)
}
```

Use this shape when:

- repeated test data should stay readable and low-noise
- the helper does not expose internal production classes or wiring
- the test still reads like behaviour, not like builder plumbing

## Example: Narrow Integration Boundary

```groovy
class CheckoutAcceptanceSpec extends IntegrationSpec implements SampleOrders {

    def "should place order through HTTP API"() {
        given: "catalog contains the ordered product"
            catalogFacade.add(validProduct())

        when: "customer places an order through the public endpoint"
            def response = webTestClient.post()
                    .uri("/checkout")
                    .bodyValue(validOrder)
                    .exchange()

        then: "system responds with approval link"
            response.expectStatus().is2xxSuccessful()
            response.expectBody()
                    .jsonPath('$.value').isEqualTo('https://payments.test/approval/payment-1')
    }
}
```

Use this shape when:

- the behaviour depends on a real transport, serialization, or framework boundary
- the behaviour is still observable through a public API, so the test can stay black-box

Prefer in this layer:

- real databases, brokers, and infrastructure when practical
- real state setup through facade or other public API when the dependency is part of the tested slice
- module-owned test fixtures when another module must seed simplified state for an integration test
- Testcontainers for infrastructure dependencies such as databases or cloud-oriented services
- WireMock or MockWebServer for HTTP dependencies only when that external system is intentionally outside the tested slice and protocol-level behaviour matters

## Example: Mock At A Module Boundary

```groovy
class CheckoutFacadeSpec extends Specification {

    def configuration = new CheckoutConfiguration()
    def payments = Mock(PaymentsFacade)
    def orders = new InMemoryOrderRepository()
    def facade = configuration.checkoutFacade(orders, payments)

    def "should request payment through the payments module"() {
        given:
        def checkout = new CheckoutCommand("user-1", BigDecimal.TEN)

        when:
        facade.checkout(checkout)

        then:
        1 * payments.startPayment({ it.userId() == "user-1" && it.total() == BigDecimal.TEN })
    }
}
```

Use this shape when:

- the test is checking an assumption about communication with another module
- interaction at the module boundary is part of the externally visible behaviour

## Keep In Mind

- prefer expressive behaviour names over class- or method-shaped names
- do not default to one spec per production class
- avoid asserting incidental internal interactions when an externally visible outcome is enough
- do not expose internals only to make mocking easier
- prefer module configuration or an equivalent public composition entry over direct construction of internal services
- do not inspect repository internals when testing through the module entry point
- keep integration tests black-box unless the repository itself is the explicit subject under test
- minimize mocks in integration and acceptance tests, and prefer realistic simulation tools when a real dependency cannot be part of the test scope
- if a dependency belongs to the integrated slice, seed it through the real system path instead of mocking it
- when another module must prepare state for the test, use that module's facade or module-owned test fixture instead of any encapsulated non-API classes
- keep integration coverage selective and boundary-driven
