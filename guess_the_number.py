import random

difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()

if difficulty == "easy":
    max_number = 50
    max_attempts = None
elif difficulty == "medium":
    max_number = 100
    max_attempts = 10
else:
    max_number = 500
    max_attempts = 7

while True:
    attempts = 0
    secret = random.randint(1, max_number)
    won = False

    while max_attempts is None or attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between 1 and {max_number}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret:
            print(f"Correct! You got it in {attempts} attempts.")
            won = True
            break                      
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    if not won:
        print(f"Out of attempts! The number was {secret}.")

    if input("Play again? (y/n): ").lower() != "y":
        break                        