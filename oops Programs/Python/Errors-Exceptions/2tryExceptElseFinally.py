# try     : code that may fail
# except  : runs when a matching exception is raised (checked top to bottom)
# else    : runs only if try raised NOTHING (keeps the try block small)
# finally : always runs: success, exception, return, or break
from contextlib import suppress


def parse(value):
    print(f"\nparse({value!r})")
    try:
        number = int(value)
        result = 100 / number
    except ValueError as e:                   # specific handlers first
        print("  except ValueError:", e)
        return None
    except ZeroDivisionError:
        print("  except ZeroDivisionError")
        return None
    except (TypeError, OverflowError) as e:   # several types in one handler
        print("  except", type(e).__name__)
        return None
    else:
        print("  else: no exception, result =", result)
        return result
    finally:
        print("  finally: always runs (even after return)")


parse("4")
parse("abc")
parse("0")
parse(None)


def finally_wins():
    try:
        return "from try"
    finally:
        print("\nfinally runs before the function actually returns")


print(finally_wins())

# Catch-all: the `as e` object carries the details
try:
    {}["missing"]
except Exception as e:                        # catch broad types only at top level
    print("caught", type(e).__name__, e.args)

# Loop with retry
attempts = iter(["x", "y", "7"])
while True:
    raw = next(attempts)
    try:
        n = int(raw)
        break
    except ValueError:
        print("retrying, bad value", raw)
print("got", n)

# Ignore an expected exception concisely
with suppress(FileNotFoundError):
    open("no_file.txt")
print("suppress() swallowed FileNotFoundError")

# with + files: the file is closed even if an exception happens inside
import os, tempfile
path = os.path.join(tempfile.gettempdir(), "exc_demo.txt")
try:
    with open(path, "w") as fh:
        fh.write("data")
        raise RuntimeError("boom inside with")
except RuntimeError as e:
    print(e, "| file closed:", fh.closed)
finally:
    os.remove(path)
