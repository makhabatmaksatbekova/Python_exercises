"""
    Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
    For practice, write this code inside a function.
"""

a = [5, 10, 15, 20, 25]
# b = []

# def first_last(l):
#     for i in range(len(l)):
#         if i == 0 or len(l)-1 == i: 
#             b.append(l[i])
            
#     return b

# print(first_last(a))

#without creatig a new list 
def first_last(l):
    return [l[0],l[-1]]

print(first_last(a))