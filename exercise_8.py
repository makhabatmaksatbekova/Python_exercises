"""
    Make a two-player Rock-Paper-Scissors game. 
    (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
    and ask if the players want to start a new game)

    Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""
import random 

again = 'yes'
while again == 'yes':
    player = input("Give 'r' for rock, 'p' for paper and 's' for scissors: ")
    if (player != 'r') and (player != 'p') and (player !='s'):
        print("Invalid input.") 
    else:
        game = ['r', 'p', 's']
        computer = random.choice(game)
        if player == computer: 
            print(f"It's a tie. Computer chose {computer} ") 
    
        elif (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
            again = (input(f"You won! Computer chose {computer}\nDo you want to play again: (yes/no) "))
    
        else:
            again = (input(f"You lost! Computer chose {computer}\nDo you want to play again: (yes/no) "))
print("Thanks for playing")





# import sys

# user1 = input("What's your name?")
# user2 = input("And your name?")
# user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
# user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

# def compare(u1, u2):
#     if u1 == u2:
#         return("It's a tie!")
#     elif u1 == 'rock':
#         if u2 == 'scissors':
#             return("Rock wins!")
#         else:
#             return("Paper wins!")
#     elif u1 == 'scissors':
#         if u2 == 'paper':
#             return("Scissors win!")
#         else:
#             return("Rock wins!")
#     elif u1 == 'paper':
#         if u2 == 'rock':
#             return("Paper wins!")
#         else:
#             return("Scissors win!")
#     else:
#         return("Invalid input! You have not entered rock, paper or scissors, try again.")
#         sys.exit()

# print(compare(user1_answer, user2_answer))