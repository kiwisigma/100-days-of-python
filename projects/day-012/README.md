# Day 12 — Scope & Number Guessing Game

## What I Built
A Number Guessing Game (`number_guesser.py`) where the player tries to guess a random number between 1–100 on easy or hard mode, with a limited number of attempts per difficulty.

## Concepts Practiced
- Local vs global scope — variables defined inside a function don't exist outside it
- The `global` keyword to modify a global variable from within a function
- Global constants (naming convention: `ALL_CAPS`) like `PI` and `GOOGLE_URL`
- Scope drills: passing return values between functions, loops with counters

## How to Run
```bash
python number_guesser.py
```

## Notes
- `range(1, 20)` does not include 20 — off-by-one scope pitfall that previews Day 13 debugging
- Global constants should never be modified; they're read-only by convention
