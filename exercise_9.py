"""
    Generate a random number between 1 and 9 (including 1 and 9). 
    Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
    (Hint: remember to use the user input lessons from the very first exercise)

    Extras:
    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random 

random_number = random.randint(1,10)
guess = 0
count = 0

while random_number != guess and guess != "exit":
    guess = input("Guess a number between 1 nd 9 or type 'exit': ")
    if guess == 'exit':
        break 
    guess = int(guess)
    count += 1

    if guess < random_number: 
        print(f"Your number {guess} is too low")
    elif guess > random_number:
        print(f"Your number {guess} is too high")
    else: 
        print(f"You got correct number {guess} \n And it only took you {count} times. ")
        
