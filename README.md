# 🎮 Python Mini Games

A collection of command-line games written in Python.

## Games

### 1. Number Guessing Game (`guess_the_number.py`)
The computer picks a secret number and you try to guess it.

**Features**
- Three difficulty levels: Easy (1–50, unlimited), Medium (1–100, 10 guesses), Hard (1–500, 7 guesses)
- Rejects invalid and out-of-range input without using an attempt
- Play-again option

### 2. Tic-Tac-Toe — *coming soon*
### 3. Quiz App — *coming soon*

## How to run
Requires Python 3.10+.

```bash
python guess_the_number.py
```

## Concepts used
- **Input validation:** `try/except ValueError` catches non-numeric input, and a range check rejects numbers outside the allowed range. Invalid input never costs the player an attempt.
- **Small, single-purpose functions:** `choose_difficulty()`, `get_guess()`, `play_game()` and `main()` each handle one job, which makes bugs easy to locate.
- **Data-driven configuration:** difficulty levels live in a dictionary of `(max_number, max_attempts)` tuples, so adding a new mode is a one-line change.
- **Control flow:** `while` loops with `continue` to retry input, and `return` to end a round and report the result in one step.
- **Local variables:** game state like `secret` and `attempts` is created inside `play_game()`, so every new round starts fresh automatically.

## Challenges
- **Indentation bug:** a `continue` was indented at the same level as `try/except` instead of inside `except`, so it ran on every guess and the game looped forever. In Python, indentation defines which block a line belongs to.
- **State leaking between rounds:** an early version tracked wins with a flag outside the game loop, so a win in one round carried into the next. Moving each round into its own function fixed this, because local variables reset on every call.
