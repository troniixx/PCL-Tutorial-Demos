import random

# Randomly select a number between 1 and 10
number_to_guess = random.randint(1, 10)
guess = None
attempts = 0

print("Guess the number between 1 and 10!")

# While loop for guessing
while guess != number_to_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
