# JUnit Examples

## Purpose

- optional cold-loaded examples showing the backend-testing strategy in JUnit-style syntax

## Use This File When

- the task needs concrete JUnit examples for behaviour-focused tests
- the task involves translating the generic testing strategy into JUnit structure

## Example: Behaviour At A Module API Boundary

```java
class OrderFacadeTest {

    private final OrderFacade facade = new OrderConfiguration().orderFacade();

    @Test
    void shouldRegisterPendingOrderAndReturnApprovalLink() {
        // when
        ApprovalLinkDto result = facade.newOrder(SampleOrders.validOrder());

        // then
        assertThat(result.value()).isEqualTo("https://payments.test/approval/payment-1");
    }

    @Test
    void shouldRejectEmptyOrder() {
        // expect
        assertThatThrownBy(() -> facade.newOrder(SampleOrders.emptyOrder()))
                .isInstanceOf(IllegalOrderStateException.class);
    }
}
```

Use this shape when:

- the module can be created through a public configuration entry such as `new OrderConfiguration().orderFacade()`
- test collaborators can be supplied through configuration when needed without exposing internal service wiring
- assertions stay on observable behaviour exposed by the facade

## Example: Shared Sample Data Helper

```java
final class SampleOrders {

    private SampleOrders() {
    }

    static OrderDto validOrder() {
        return new OrderDto(
                "user-1",
                Set.of(new OrderDto.ProductDto(UUID.fromString("11111111-1111-1111-1111-111111111111"), 2))
        );
    }

    static OrderDto emptyOrder() {
        return new OrderDto("user-1", Set.of());
    }
}
```

Use this shape when:

- repeated test data should stay readable and low-noise
- the helper does not expose internal production classes or wiring
- the test still reads like behaviour, not like builder plumbing

## Example: Narrow Integration Boundary

```java
class CheckoutAcceptanceTest extends IntegrationTestBase {

    @Test
    void shouldPlaceOrderThroughHttpApi() {
        // given
        catalogFacade.add(validProduct());

        // expect
        webTestClient.post()
                .uri("/checkout")
                .bodyValue(SampleOrders.validOrder())
                .exchange()
                .expectStatus().is2xxSuccessful()
                .expectBody()
                .jsonPath("$.value").isEqualTo("https://payments.test/approval/payment-1");
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

```java
class CheckoutFacadeTest {

    private final CheckoutConfiguration configuration = new CheckoutConfiguration();
    private final PaymentsFacade payments = mock(PaymentsFacade.class);
    private final InMemoryOrderRepository orders = new InMemoryOrderRepository();
    private final CheckoutFacade facade = configuration.checkoutFacade(orders, payments);

    @Test
    void shouldRequestPaymentThroughPaymentsModule() {
        // given
        CheckoutCommand checkout = new CheckoutCommand("user-1", BigDecimal.TEN);

        // when
        facade.checkout(checkout);

        // then
        verify(payments).startPayment(argThat(command ->
                command.userId().equals("user-1") && command.total().compareTo(BigDecimal.TEN) == 0));
    }
}
```

Use this shape when:

- the test is checking an assumption about communication with another module
- interaction at the module boundary is part of the externally visible behaviour

## Keep In Mind

- prefer behaviour-oriented test names over names tied to internal methods
- do not default to one test class per production class
- avoid asserting incidental internal interactions when an externally visible outcome is enough
- do not expose internals only to make mocking easier
- prefer module configuration or an equivalent public composition entry over direct construction of internal services
- do not inspect repository internals when testing through the module entry point
- keep integration tests black-box unless the repository itself is the explicit subject under test
- minimize mocks in integration and acceptance tests, and prefer realistic simulation tools when a real dependency cannot be part of the test scope
- if a dependency belongs to the integrated slice, seed it through the real system path instead of mocking it
- when another module must prepare state for the test, use that module's facade or module-owned test fixture instead of any encapsulated non-API classes
- keep integration coverage selective and boundary-driven
