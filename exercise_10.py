"""
    Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
    Make sure your program works on two lists of different sizes. 
    Write this in one line of Python using at least one list comprehension.
    In general, the list comprehension takes the form:

	[EXPRESSION FOR_LOOPS CONDITIONALS]
"""
# import random
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# # a = random.sample(range(50),7) # random.sample genertes unique characters
# # b = random.sample(range(50),10)

# # a = random.choices(range(50),7)
# # b = random.choices(range(50),10)
# c = [x for x in a if x in b]


# print(c)

# cookies = True 
# cake = False 
# if cookies:
#     print("OMG COOKIEZ")

# if cake:
#     print("OMG CAKE!")
# else:
#     print("WHATEVZ DESSERTZ.")