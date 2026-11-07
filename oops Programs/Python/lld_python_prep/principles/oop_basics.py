from abc import ABC, abstractmethod


class Account:
    """Encapsulation: callers cannot directly set an invalid balance."""
    def __init__(self, owner: str, opening_balance: float = 0) -> None:
        self.owner = owner
        self._balance = opening_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount


class PaymentMethod(ABC):  # abstraction
    @abstractmethod
    def pay(self, amount: float) -> str: ...


class Card(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"charged card: {amount:.2f}"


class UPI(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"paid via UPI: {amount:.2f}"


def checkout(method: PaymentMethod, amount: float) -> str:
    return method.pay(amount)  # polymorphism


if __name__ == "__main__":
    account = Account("Raghav", 100)
    account.deposit(50)
    print(account.balance)
    print(checkout(UPI(), 99))
