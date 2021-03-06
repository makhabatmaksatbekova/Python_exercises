"""
    Ask the user for a number and determine whether the number is prime or not. 
    (For those who have forgotten, a prime number is a number that has no divisors.). 
    You can (and should!) use your answer to Exercise 4 to help you. 
    Take this opportunity to practice using functions, described below.
"""

def ask_user():
    return int(input("Give me a number: "))

def is_prime():
    num = ask_user()
    
    if num < 2:
        return (f"{num} is not a prime number ")
    else: 
        for i in range(2,num):
            if num % i == 0:
                return(f"{num} is divisible by {i}")
                
    
        return(f"{num} is a prime number")




print(is_prime())