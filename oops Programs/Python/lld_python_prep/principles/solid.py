from abc import ABC, abstractmethod
from dataclasses import dataclass


# Single responsibility: Invoice only holds data; formatter owns presentation.
@dataclass
class Invoice:
    customer: str
    amount: float


class InvoiceFormatter:
    def format(self, invoice: Invoice) -> str:
        return f"{invoice.customer}: Rs {invoice.amount:.2f}"


# Open/closed + dependency inversion: new discounts implement the abstraction.
class Discount(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float: ...


class PercentageDiscount(Discount):
    def __init__(self, percent: float) -> None:
        self.percent = percent

    def apply(self, amount: float) -> float:
        return amount * (1 - self.percent / 100)


class Checkout:
    def __init__(self, discount: Discount) -> None:
        self.discount = discount

    def total(self, amount: float) -> float:
        return self.discount.apply(amount)


# Interface segregation: small focused interfaces instead of one giant Worker API.
class Printable(ABC):
    @abstractmethod
    def print_document(self, text: str) -> None: ...


class BasicPrinter(Printable):
    def print_document(self, text: str) -> None:
        print(text)


if __name__ == "__main__":
    print(InvoiceFormatter().format(Invoice("Asha", Checkout(PercentageDiscount(10)).total(1000))))
