# raise: throw an exception yourself (like C++ throw / Java throw).


def withdraw(balance, amount):
    if not isinstance(amount, (int, float)):
        raise TypeError(f"amount must be a number, got {type(amount).__name__}")
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError(f"insufficient funds: balance {balance}, requested {amount}")
    return balance - amount


for amt in (30, -5, 500, "10"):
    try:
        print("new balance:", withdraw(100, amt))
    except (ValueError, TypeError) as e:
        print(f"{type(e).__name__}: {e}")


# Re-raise: log/clean up, then let the caller handle it. Bare `raise` keeps the traceback.
def load(cfg):
    try:
        return cfg["port"]
    except KeyError:
        print("load(): missing key, re-raising")
        raise


try:
    load({})
except KeyError as e:
    print("caller got KeyError", e)

# raise a class (instantiated automatically) or an instance
try:
    raise NotImplementedError
except NotImplementedError as e:
    print("NotImplementedError", repr(e))


class Shape:
    def area(self):
        raise NotImplementedError("subclasses must implement area()")


try:
    Shape().area()
except NotImplementedError as e:
    print(e)

# Exceptions are objects: extra args are kept in .args
try:
    raise ValueError("bad", 42)
except ValueError as e:
    print(e.args)
