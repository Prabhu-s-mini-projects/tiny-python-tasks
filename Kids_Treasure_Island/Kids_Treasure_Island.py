print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to Treasure Island. \n")
print("Your mission is to find a Treasure.\n")
chosen_path = input('you\'re at the cross Road. Where do you want to go? \n"left" or "Right" :\t')
if chosen_path.lower() == "left":
    chosen_path = input('\nYou\'ve reached the River side.How do you prefer to proceed?\n"Swim" or "wait" for boat :\t')
    if chosen_path.lower() == "wait":
        chosen_path = input('\nYou\'ve arrived at the island.There is a house with 3 doors. "READ" "BLUE" "YELLOW"  :\t')
        if chosen_path.lower() == 'read':
            print("\nYou're Burned alive.\n\n GAME OVER ~!")
        elif chosen_path.lower() == 'blue':
            print("\nYou're entered into room full of ANGRY BEASTS.\n\n GAME OVER ~!")
        elif chosen_path.lower() == 'yellow':
            print('''
                                       _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \\'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
            ''')
            print("\nCONGRATULATIONS.\n\n You FOUND the TREASURE :-).")
        else:
            print(f"\nThere are no door colored {chosen_path.lower()}.")
            print("\nTreasure Protector through you into river.\n\n GAME OVER ~!")
    else:
        print("\nYou got attacked by SEA MONSTER.\n\n GAME OVER ~!")
else:
    print("\nYou have FELL into HOLE.\n\n GAME OVER ~!")

