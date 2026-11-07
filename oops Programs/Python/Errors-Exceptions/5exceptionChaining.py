# Exception chaining links a new exception to the one that caused it.
#   raise New from old  -> explicit cause   (__cause__),  "direct cause" in traceback
#   raise New (in except) -> implicit context (__context__), "During handling ..."
#   raise New from None -> hide the original
import sys
import traceback


class ConfigError(Exception):
    pass


def read_port(cfg):
    try:
        return int(cfg["port"])
    except KeyError as e:
        raise ConfigError("port is not configured") from e      # explicit
    except ValueError:
        raise ConfigError("port is not a number")               # implicit


def read_port_quiet(cfg):
    try:
        return int(cfg["port"])
    except (KeyError, ValueError):
        raise ConfigError("invalid port") from None             # suppressed


for cfg in ({}, {"port": "abc"}):
    try:
        read_port(cfg)
    except ConfigError as e:
        print(f"{e!r}")
        print("   __cause__  :", repr(e.__cause__))
        print("   __context__:", repr(e.__context__))

try:
    read_port_quiet({})
except ConfigError as e:
    print(f"{e!r} cause={e.__cause__!r} suppress_context={e.__suppress_context__}")

print("\n--- full chained traceback (printed, not raised) ---")
try:
    read_port({})
except ConfigError:
    traceback.print_exc(limit=1, file=sys.stdout)
