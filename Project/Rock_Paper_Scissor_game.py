"""
    Rock Paper Scissor Game

    In this game, we
    
    1. play against the computer
    computer will choose a random (rock, paper, scissor).
    2) Input From user (rock, paper, scissor)
    3) Print result (Win, Lose, Draw)
    
Concept of Python Used here:

1)Manipulation of list
2)Condition
3)Function Uses
4)How to Generate Random values 
5)Convert input to upperCase or LowerCase



WorkFLow of the project:

1) Input From user (Rock,Paper, Scissor)
2) Computer will choose a random (rock, paper, scissor)
3) Print result (Win, Lose, Draw)


Conditions (A = Rock, B = Paper, C = Scissor)


Condition For A (Rock)

Rock vs Rock = Draw
Rock vs paper = paper Win
Rock vs scissor = Rock Win

Condition For B (Paper)

paper vs paper = Draw
paper vs scissor = Scissor Win
paper vs rock = Paper Win

Condition for C (Scissor)

scissor vs scissor = Draw
scissor vs paper = Scissor Win
scissor vs rock = Rock Win
    
    
"""

import random

def rock_paper_scissor_game():
    # making list 
    items_list = ["rock","paper","scissor"]
    
    # taking input
    user_input = input("Choose Rock, paper, scissor : ").lower()
    comp_choices = random.choice(items_list)
    
    print(f"\nYour Choice : {user_input} \nComputer Choice : {comp_choices}")
    
    if user_input == comp_choices:
        return False
    
    elif user_input == 'rock':
      
        if comp_choices =='paper':
            return 'lose'
        elif comp_choices == 'scissor':
            return 'win'
        
    elif user_input == 'paper':
        if comp_choices =='rock':
            return 'win'
        elif comp_choices == 'scissor':
            return 'lose'
        
    elif user_input == 'scissor':
        if comp_choices =='paper':
            return 'win'
        elif comp_choices == 'rock':
            return 'lose'
    else:
        print("Invalid Entry")

game_output =  rock_paper_scissor_game() 

if game_output == False:
    print ("Draw")
elif game_output == 'win':
    print ("You Win")
elif game_output == 'lose':
    print ("You Lose")
else:
    print("Invalid Entry")
