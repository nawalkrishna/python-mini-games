import random

DIFFICULTIES = {
    "easy": (50, None),
    "medium": (100, 10),
    "hard": (500, 7),
}


def choose_difficulty():
    """Ask until the player picks a valid difficulty. Returns (max_number, max_attempts)."""
    while True:
        choice = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Choose easy, medium or hard.")


def get_guess(max_number):
    """Ask until the player types a whole number in range. Returns the guess."""
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_number}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= guess <= max_number:
            return guess
        print(f"Please guess between 1 and {max_number}.")


def play_game(max_number, max_attempts):
    """Play one round. Returns True if the player won, False if not."""
    secret = random.randint(1, max_number)
    attempts = 0

    while max_attempts is None or attempts < max_attempts:
        guess = get_guess(max_number)
        attempts += 1

        if guess == secret:
            print(f"Correct! You got it in {attempts} attempts.")
            return True
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Out of attempts! The number was {secret}.")
    return False


def main():
    max_number, max_attempts = choose_difficulty()

    while True:
        play_game(max_number, max_attempts)
        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()