"""
    Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list
     minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""


# this solution works only for sorted lists 
# def remove_duplicates(l):
#     no_duplicates = []
#     current = 0
#     next_el = 0

#     for i in range(len(l)): 
#         if l[current]==l[next_el]:
#           next_el = next_el + 1
#         if next_el == len(l):
#            no_duplicates.append(l[current])
#            return no_duplicates 
#         if l[current] != l[next_el]:
#             no_duplicates.append(l[current])
#             current = next_el
#     return no_duplicates


# print(remove_duplicates([1,1,1,2,4,4,5,5,5]))

# def remove_duplicates(l):
#     no_duplicates = set(l)
#     no_duplicates = list(no_duplicates)
#     return no_duplicates


# print(remove_duplicates([1,1,1,2,4,4,5]))

def remove_dup(l):
    no_duplicates = []
    for i in l:
        if i not in no_duplicates:
            no_duplicates.append(i)
    return no_duplicates

print(remove_dup([1,1,1,2,4,4,5,1,2]))