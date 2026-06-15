# Day 10 — Calc-U-Later 3000

## What I Built
A command-line calculator that supports addition, subtraction, multiplication, and division. After each calculation the user can continue using the result as the next input, or start fresh.

## Concepts Practiced
- Functions with return values
- Dictionaries storing functions as values
- While loops for continuous calculation
- Recursion to restart the calculator
- f-strings for formatted output

## How to Run
```bash
python Calc-U-Later_3000.py
```

## Notes
- Operations are stored in a dictionary mapping symbols (`+`, `-`, `*`, `/`) to their functions
- Typing `y` chains the result into the next calculation; `n` restarts
