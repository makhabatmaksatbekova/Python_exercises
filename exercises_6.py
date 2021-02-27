"""
    Ask the user for a string and print out whether this string is a palindrome or not. 
    (A palindrome is a string that reads the same forwards and backwards.)
"""

user_str = input("Give me a string: ")

if user_str == user_str[::-1]:
    print(f"{user_str} is a palindrome")
else:
    print(f"{user_str} is not a palindrome")
