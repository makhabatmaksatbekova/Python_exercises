import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"


# complete the program here

play = True 
while play == True:
    player1 = choose_rps()
    print(f"player1 chose {player1}")
    player2 = choose_rps()
    print(f"player2 chose {player2}")
    
    if player1 == player2:
    # if (player1 == 'paper' and player2 == 'paper') or (player1 == 'rock' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'scissors'):
        print('It\'s a tie!')
    elif player2 == 'rock':
        if player1 == 'scissors':
            print('Player 2 won!')
        else:
            print('Player 1 won!')
    elif player2 == "paper":
        if player1 == 'rock':
            print("Player 2 won!")
        else:
            print("player 1 won!")
    elif player2 == 'scissors':
        if player1 == 'rock':
            print('Player 2 won!')
        else:
            print('Player 1 won!')
    play = input("Do you want to play again: yes  or no:  ")
    if play == "yes":
        play =  True 
    else: 
        print("Thanks for playing")


## examples of creating helper functions 

import random

def choose_rps():
  r = random.randint(0,2) #returns random number 0 to 2
  
  if r == 0:
      return "rock" # 0 = rock
  elif r == 1:
      return "scissors" # 1 = scissors
  else:
      return "paper" # 2 = paper

def rps_function(player1, player2):
  # tie
  if player1 == player2:
    print("It's a tie!")
  # player1 = scissors
  elif player1 == "scissors":
    if player2 == "rock":
      print ("Player 2 won!")
    else:
      print("Player 1 won!")
    # player1 = rock
  elif player1 == "rock":
    if player2 == "scissors":
      print ("Player 1 won!")
    else:
      print("Player 2 won!")
  # player1 = paper
  else:
    if player2 == "scissors":
      print ("Player 2 won!")
    else:
      print("Player 1 won!")
       

def play_again():
  r = random.randint(0,1)
  if r == 0:
    return True
  else:
    return False

play = True

print("Welcome to Rock, Paper, Scissors!\n")
while play == True:
  player1 = choose_rps()
  player2 = choose_rps()

  print("Player 1 chose", player1, ".")
  print("Player 2 chose", player2, ".")

  rps_function(player1, player2)

  print(" ")

  play = play_again()

print("Thank you for playing!")      
