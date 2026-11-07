from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self) -> int: ...


class SimpleCoffee(Coffee):
    def cost(self) -> int: return 100


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee) -> None: self.coffee = coffee


class Milk(CoffeeDecorator):
    def cost(self) -> int: return self.coffee.cost() + 30


class Whip(CoffeeDecorator):
    def cost(self) -> int: return self.coffee.cost() + 20


if __name__ == "__main__":
    print(Whip(Milk(SimpleCoffee())).cost())
