# Day 13 — Debugging

## What I Built
A series of debugging exercises — no single app, but six broken programs fixed by identifying logic errors, off-by-one mistakes, type mismatches, and scope bugs.

## Concepts Practiced
- Describing the problem before touching code (task1)
- Off-by-one errors — `range(1, 20)` never reaches 20 (task1)
- Logic/condition errors — missing generation bracket in birth-year classifier (task3)
- `try/except ValueError` for bad user input (task4)
- Variable initialization order and unused variables (task5)
- Importing and calling functions from another module (`maths.py`) correctly (task6)
- Fixing leap year logic with nested `if` conditions (exercise1)
- Correcting FizzBuzz divisibility order — `FizzBuzz` check must come before `Fizz`/`Buzz`

## How to Run
```bash
python task1_debugging.py   # off-by-one demo
python task6.py             # mutate list with imported maths module
```

## Notes
- Debugging mindset: reproduce → describe → isolate → fix, don't just guess and change things
- `range(1, 20)` stops at 19; use `range(1, 21)` to include 20
