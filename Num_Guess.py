"""This is a simple number guessing game where the user has to guess a randomly generated number within a specified range."""
import random
GAME_RUNNING = True
LOWER_BOUND = 1
UPPER_BOUND = 100
NUMBER_TO_GUESS = random.randint(LOWER_BOUND, UPPER_BOUND)
MAX_ATTEMPTS = 10
attempts = 0
print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}. You have {MAX_ATTEMPTS} attempts to guess it.")
while GAME_RUNNING and attempts < MAX_ATTEMPTS:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        if user_guess < LOWER_BOUND or user_guess > UPPER_BOUND:
            print(f"Please guess a number within the range of {LOWER_BOUND} to {UPPER_BOUND}.")
            continue
        if user_guess < NUMBER_TO_GUESS:
            print("Too low! Try again.")
        elif user_guess > NUMBER_TO_GUESS:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {NUMBER_TO_GUESS} correctly in {attempts} attempts.")
            GAME_RUNNING = False
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
