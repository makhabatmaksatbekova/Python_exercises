"""
    4. Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
    (If you don’t know what a divisor is, 
    it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

# user_number = int(input("Give me a number: "))
# divisors_list = []

# numbers_list = list(range(1, user_number+1))
# for item in numbers_list:
#     if user_number % item == 0:
#         divisors_list.append(item)
# print(divisors_list)

import random

def play_again():
    r = random.randint(0, 1)

    return r == 0

again = True
while again:
    print("Let's play a game!")
    print("...")
    again = play_again()

print("Game Over!")