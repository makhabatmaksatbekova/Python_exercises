# Here is my solutions for small beginning level exercises on python

#1 ////////////
# name = input("What is your name? ")
# age = int(input("What is your age "))
# current_year = 2021

# year_100 = (100-age)+ 2021

# print(f"You will turn 100 in {year_100}.")

# adjective = input("Give me an adjective ")
# number = int(input("Give me a number: "))
# me = (f"I am a {adjective} girl!\n")
# result = me * number
# print(result)

#2//////////Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# user_number = int(input("Give me a number: "))
# divider = int(input("Give me number to divide: "))

# if user_number % 4 == 0:
#   print(f"Your given number {user_number} is multiple of four.")
# elif user_number % 2 == 0:
#   print(f"Your given number {user_number} is even.")
# else:
#   print(f"Your given number {user_number} is odd.")


# if user_number % divider == 0:
#   print(f"Your {user_number} is dividible by {divider}.")
# else:
#   print(f"Your {user_number} is not divible by {divider} ")

#3///  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


user_number = int(input("Give me a number: "))
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_5 = []
new_list = []


for item in my_list:
  if item < 5:
    less_than_5.append(item)

print(less_than_5)

for item in my_list:
    if item < user_number:
        new_list.append(item)

print(new_list)