# Custom exceptions: subclass Exception (not BaseException).
# Build a small hierarchy so callers can catch one base or a specific child.


class BankError(Exception):
    """Base class for all errors in this module."""


class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance                 # extra data for the handler
        self.amount = amount
        super().__init__(f"need {amount - balance} more (balance {balance}, requested {amount})")


class AccountFrozenError(BankError):
    pass


class Account:
    def __init__(self, owner, balance=0, frozen=False):
        self.owner = owner
        self.balance = balance
        self.frozen = frozen

    def withdraw(self, amount):
        if self.frozen:
            raise AccountFrozenError(f"{self.owner}'s account is frozen")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


accounts = [Account("Raghav", 100), Account("Amit", 20), Account("Bina", 500, frozen=True)]
for acc in accounts:
    try:
        print(acc.owner, "left with", acc.withdraw(50))
    except InsufficientFundsError as e:        # specific first
        print(acc.owner, "->", type(e).__name__, ":", e, "| shortfall:", e.amount - e.balance)
    except BankError as e:                     # then the family base
        print(acc.owner, "->", type(e).__name__, ":", e)

print(issubclass(InsufficientFundsError, BankError), isinstance(InsufficientFundsError(1, 2), Exception))


# __str__ customises the message
class ValidationError(Exception):
    def __init__(self, field, problem):
        self.field, self.problem = field, problem
        super().__init__(field, problem)

    def __str__(self):
        return f"{self.field}: {self.problem}"


try:
    raise ValidationError("email", "missing @")
except ValidationError as e:
    print(e, "|", e.args)
