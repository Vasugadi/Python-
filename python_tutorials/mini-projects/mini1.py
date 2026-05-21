#guess the number game

import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

guess_the_number()
# This code implements a simple "Guess the Number" game where the user has to guess a randomly generated number between 1 and 100.
# The user is prompted to enter their guess, and the program provides feedback on whether the guess
        

target_num=random.randint(1, 100)

print(target_num)

while True:
    user_choice = (input("Enter your guess: "))
# is too low, too high, or correct. The game continues until the user guesses the correct number.
    if user_choice == "Q":
        print("You chose to quit the game.")
        break
    if user_choice == target_num:
        print("Congratulations! You guessed the number correctly.")
        break
    elif user_choice < target_num:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
    
print("Game Over! The number was:", target_num)
# The game continues until the user guesses the correct