hi2 = input("Welcome create your account")
username = input("Enter your username")
password = input ("Enter your password")

for i in range (3,0,-1):
  attempt1=input("Enter your username and password:")
  if attempt1 == username + password :
    break
  else:
    print ("Access denied please try again you have 3 attempts")
if i == 1:
  print("You dont have access")
else:
  print("Your password and username have been granted enjoy")
#player 2




hi = input ("lets create an account")
username2 = input("Enter your username player 2")
password2 = input("Enter your password player 2")

for i in range (3,0,-1):
  P2attempt=input("Hi player 2 enter your username and password:")
  if P2attempt == username2 + password2:
    break
  else:
    print("Access denied please try again")
if i == 1:
  print("You dont have access")
else:
  print("Welcome player 2 enjoy your game")


print ("Player 1 your dices are rolling ...")
import random
def diceroll():
 dice1=random.randint(1,6)
 dice2=random.randint(1,6)
 return dice1 , dice2

import random
def Double ():
 doubler = random.randint (1,6)
 return doubler
  
# Main program actual game
def main():
  rounds = 1
  points = 0
  while rounds != 6:
    print ("Round" , rounds)
    player1 = diceroll()
    player2 =diceroll()
    print ("player1 you rolled ", player1 )
    print("Player2 you rolled", player2 )
    points=0
    totalscr1 = points + player1[0] + player1[1]
    totalscr2= points + player2[0] + player2[1]
    print ("Player1 you scored a total of:", totalscr1)
    print("Player2 you scored a total of:" ,totalscr2)
    if totalscr1 / 2 :
      print (" PLayer 1 You get 10 points")
    else:
      print(" PLayer 1 thats minus 5 points")

    if totalscr2 // 2:
      print("Player 2 you get another 10 points")
    else:
      print("Player 2 thats minus 5 points ")


    
    if totalscr1 > totalscr2:
      print ("Player one you have won")
    elif totalscr1 == totalscr2:
      print("You drew ")
    else:
      print("Player 2 you won ")
    
    rounds = rounds + 1
    
print(main()) 




    
