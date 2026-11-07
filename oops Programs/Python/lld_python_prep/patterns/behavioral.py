from abc import ABC, abstractmethod
from typing import Callable


class PricingStrategy(ABC):
    @abstractmethod
    def price(self, base: float) -> float: ...


class Regular(PricingStrategy):
    def price(self, base: float) -> float: return base


class Festival(PricingStrategy):
    def price(self, base: float) -> float: return base * 0.8


class Cart:
    def __init__(self, strategy: PricingStrategy) -> None:
        self.strategy = strategy

    def total(self, base: float) -> float:
        return self.strategy.price(base)


class EventBus:
    """Observer: producers do not need to know their subscribers."""
    def __init__(self) -> None:
        self._listeners: list[Callable[[str], None]] = []

    def subscribe(self, listener: Callable[[str], None]) -> None:
        self._listeners.append(listener)

    def publish(self, event: str) -> None:
        for listener in self._listeners:
            listener(event)


if __name__ == "__main__":
    print(Cart(Festival()).total(500))
    bus = EventBus(); bus.subscribe(print); bus.publish("order_placed")
