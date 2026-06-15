# Day 11 — Blackjack

## What I Built
A command-line Blackjack game where you play against the computer. Deals two cards each, lets you hit or pass, then the computer plays to 17 and the winner is determined.

## Concepts Practiced
- Functions with parameters and return values
- Lists and `.append()` for managing hands
- `random.choice()` for dealing cards
- `sum()` for calculating scores
- While loops for game flow
- ASCII art imported from a separate module

## How to Run
```bash
python blackjack.py
```

## Notes
- Ace (11) automatically converts to 1 if the hand goes over 21
- A two-card 21 is treated as Blackjack (score returned as 0)
- Computer always hits until it reaches 17 or higher
- Game can be replayed without restarting the script
