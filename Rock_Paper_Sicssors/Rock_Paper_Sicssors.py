# Rock Paper Scissors
import random

# References:
# Scissors:  https://www.asciiart.eu/people/body-parts/hand-gestures
# Rock & Paper: https://replit.com/@appbrewery/rock-paper-scissors-start#main.py

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
 __      __
( _\\    /_ )
 \ _\\  /_ / 
  \ _\\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \\/  ;   /
    | === |
'''

trophy = '''
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\
'''
# DB
hand_gestures = [rock, paper, scissors]

print("\nWelcome to Rock Paper Scissor game.\n")

player_name = input("\nGAME HANDLER: Player, please enter your name : \t").upper()

# Trash talk
user_trash_task = input(f"\nCOMPUTER: It's my bad time, that I have to play against a puny like you\n{player_name}:\t")
print("\nCOMPUTER: oh yeah, Lets see it in the game. Remember, I am CHAMPION in this GAME \n")

print("GAME HANDLER: Enough with Trash talk. Lets Begin the game")

# Requesting user to enter his choice
user_choice = int(input("\n Player decide the choice \n0 for Rock.\n1 for Paper.\n2 for Scissors.\n"))

# Computer decides which one to choose.
computer_choice = random.randint(0, 2)

# Reviewing the Game result.
user_win = False
if user_choice in [0, 1, 2]:

    print(f"GAME HANDLER:\t{player_name} chosen :{hand_gestures[user_choice]}")
    print(f"GAME HANDLER:\tComputer chosen: {hand_gestures[computer_choice]}")

    if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
        user_win = True
else:
    print(f"\nGAME HANDLER: You need to enter either 0 or 1 or 2 not :{user_choice}")



if user_win:
    print(f"\nGAME HANDLER: Congrats  {player_name} ! \n {trophy} \nYou're the new champion.\n")
elif user_choice == computer_choice:
    print(f"\nGAME HANDLER: Coincidentally, Both {player_name} and COMPUTER chosen the same.\n\n \t GAME TIED !!")
else:
    print(f"\nGAME HANDLER: {player_name} lost the game. \n COMPUTER: Someone told me this '{user_trash_task}'. \n GOOD for trash talk only!")







