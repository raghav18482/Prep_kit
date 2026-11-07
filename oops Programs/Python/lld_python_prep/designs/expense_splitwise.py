from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class User:
    id: str


class ExpenseService:
    """Tracks net balances: positive means others owe this user."""
    def __init__(self) -> None:
        self.balances: dict[str, Decimal] = defaultdict(Decimal)

    def add_equal_expense(self, paid_by: User, participants: list[User], amount: Decimal) -> None:
        if not participants or amount <= 0: raise ValueError("invalid expense")
        share = amount / len(participants)
        for participant in participants:
            if participant != paid_by:
                self.balances[participant.id] -= share
                self.balances[paid_by.id] += share

    def balance_of(self, user: User) -> Decimal:
        return self.balances[user.id]


if __name__ == "__main__":
    a, b, c = User("A"), User("B"), User("C")
    service = ExpenseService(); service.add_equal_expense(a, [a, b, c], Decimal("300"))
    print({u.id: service.balance_of(u) for u in [a, b, c]})
