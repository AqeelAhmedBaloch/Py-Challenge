# Day-8 Challenge
from random import randint

# Generate random number between 1 and 100
secret_number = randint(1, 100)
attempts = 0

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")

while True:
    try:
        # Get user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
    except ValueError:
        print("Please enter a valid number.")