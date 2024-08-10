# We all have played snake, water gun game in our childhood.
#  If you haven’t, google the rules of this game and 
# write a python program capable of playing this game with the user.

# Game rules :
# "s" for snake, "w" for water, "g" for gun.
'''
  s  w  g
s d  s  g
w s  d  w
g g  w  d    

'''
#Let's Play the Game 

import random 
''' 
"1 for snake", 
"0 for water", 
"-1 for gun" 
'''

computer = random.choice([-1, 0, 1])

youstr = input("Choose either snake as s or water as w or gun as g: ")
youDict = {"s" : 1, "w" : 0, "g" : -1}
reverse_Dict = {1 : "snake", 0 : "water", -1 : "gun"}

you = youDict[youstr]

# By now we have two numbers (variables), you and computer

print(f"you chose {reverse_Dict[you]}\nComputer chose {reverse_Dict[computer]}")

if(computer == you):
    print("It's draw!")
'''
else:
    if(computer == 1 and you == 0):
        print("Oops!, you lose!")

    elif(computer == 1 and you == -1):
        print("Hurray!, you win!")

    elif(computer == 0 and you == -1):
        print("Oops!, you lose!")

    elif(computer == 0 and you == 1):
        print("Hurray!, you win!")

    elif(computer == -1 and you == 1):
        print("Oops!, you lose!")

    elif(computer == -1 and you == 0):
        print("Hurray!, you win!")

    else:
        print("Something went wrong!")

'''
# The below logic is written on the basis of the of value computer - you.
if((computer - you) == -1 or (computer - you) == 2 ):
    print("you lose!")

else:
    print("you win!")