# Day 15 — Coffee Machine

## What I Built
A command-line coffee machine that serves espresso, latte, or cappuccino. It
checks whether it has enough water/milk/coffee, takes payment in coins, gives
change, banks the profit, and prints a resource report on demand. Typing `off`
shuts it down (the maintainer's secret word).

## Concepts Practiced
- Nested dictionaries (`MENU` recipes + costs, `resources` inventory)
- Functions with parameters and `return` values
- Clean program structure: data → functions → loop
- `if` / `elif` / `else` branching on user choice
- Dictionary iteration to check and deduct ingredients
- f-strings with `:.2f` money formatting

## How to Run
```bash
python coffee_machine.py
```

## Notes
- Commands: a drink name to order, `report` for resource levels, `off` to quit
- Resource check happens **before** taking money; ingredients deducted only
  after payment clears
- QoL extras: shows the drink's cost before asking for coins, and a running
  total as each coin is inserted

