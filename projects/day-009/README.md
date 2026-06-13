# Day 9 — Silent Auction

## What I Built
A silent auction program that collects bids from multiple users, stores them in a dictionary, then finds and announces the highest bidder. Clears the screen between bidders so no one sees each other's bids.

## Concepts Practiced
- Dictionaries (storing and accessing key-value pairs)
- Iterating over a dictionary
- Functions with dictionary parameters
- While loops for collecting multiple inputs

## How to Run
```bash
python Silent_Auction.py
```

## Notes
Screen is "cleared" by printing 20 newlines — a simple trick before learning `os.system('clear')`. The `find_highest_bidder` function manually iterates to find the max rather than using `max()` directly on the dictionary.
