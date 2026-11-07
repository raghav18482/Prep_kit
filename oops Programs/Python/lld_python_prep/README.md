# Python LLD Prep Kit

Run every example from this directory with `python3 path/to/file.py`.

## Suggested learning order

1. `principles/oop_basics.py` — encapsulation, abstraction, inheritance, polymorphism
2. `principles/solid.py` — the five SOLID principles
3. `patterns/` — reusable object collaboration patterns
4. `designs/` — interview-style machine coding designs

## What to practise for each design

- Identify entities, responsibilities, and relationships.
- Model state changes explicitly and protect invariants.
- Prefer composition over inheritance unless the relationship is truly “is-a”.
- Make dependencies injectable so behaviour can be tested or swapped.
- Add concurrency, persistence, APIs, and error handling only after the core model is correct.

The code is deliberately compact and in-memory: it teaches design, not framework setup.
