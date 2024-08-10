'''We are going to write a program that generates a random number and asks the user to guess it.
If the player’s guess is higher than the actual number, the program displays “Lowernumber please”. 
Similarly, if the user’s guess is too low, the program prints “higher number please” 
When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.'''

import random 
n = random.randint(15, 98)

a = -1
guesses = 0
while (a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    if(a > n):
        print("Guess Lower number please")

    else:
        print("Guess Higher number please")


print(f"You have guessed the number {n} correctly in {guesses} attempt")


# Chatgpt Suggestions
'''
import random

def guess_the_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    guess = None
    number_of_guesses = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user guesses the correct number
    while guess != target_number:
        try:
            # Ask the user for a guess
            guess = int(prompt())
            number_of_guesses += 1

            # Provide feedback on the guess
            if guess < target_number:
                print("Higher number please.")
            elif guess > target_number:
                print("Lower number please.")
            else:
                print(f"Congratulations! You've guessed the correct number: {target_number}")
                print(f"It took you {number_of_guesses} guesses.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def prompt():
    return input("Enter your guess: ")

# Run the game
guess_the_number()
'''
#Explanantion
'''
Importing the random Module:
The random module is used to generate a random number.
Generating a Random Number:
The program generates a random number between 1 and 100 using random.randint(1, 100).

Initializing Variables:
guess is initialized to None to store the user's guess.
number_of_guesses is initialized to 0 to count the number of guesses made by the user.

Game Loop:
The loop continues until the user guesses the correct number (guess != target_number).
Inside the loop, the user is prompted to enter a guess.

The program checks if the guess is lower, higher, or equal to the target number and provides appropriate feedback.

If the user guesses the correct number, the program congratulates the user and displays the total number of guesses made.

Error Handling:
The program includes a try block to handle invalid inputs (non-integer values) gracefully, prompting the user to enter a valid number.

This code will allow the user to play a simple number guessing game, with the program guiding them toward the correct answer.'''
    

    




