# Day 14 — Higher Lower Game

## What I Built
A guessing game that shows two public figures and asks which one has more
Instagram followers. Guess right and your score climbs and the winner carries
over to the next round; guess wrong and the game ends with your final score.

## Concepts Practiced
- Lists of dictionaries (each account stored as a dict)
- Dictionary access with bracket notation inside f-strings
- `random.choice()` to pick accounts
- `while` loops for the game round flow
- Score tracking and comparison logic

## How to Run
```bash
python higher_lower.py
```

## Notes
- The previous round's winner becomes the next round's "A" so comparisons chain
- Logic guards against comparing the same account against itself
