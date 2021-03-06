"""
    Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
    Take this opportunity to think about how you can use functions. 
    Make sure to ask the user to enter the number of numbers in the sequence to generate.
    (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def user_input():
    return int(input("How many Fibonnaci numbers generate?: "))

def fibonnaci():
    number = user_input()

    fib_list = []
    current = 1
    next_num = 1

    for i in range(1, number+1):
        s = current + next_num
        fib_list.append(current)
        current = next_num
        next_num = s

    return fib_list

print(fibonnaci())