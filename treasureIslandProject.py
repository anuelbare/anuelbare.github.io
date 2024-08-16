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
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island adventurer!!!!\n Your mission is to find the treasure.")
print("You find yourself at a cross road. Which path would you like to take? ")
direction = input("        Type \"left\" or \"right\". ")
if direction == "left" or direction == "Left" or direction == "LEFT":
    print("You find yourself at a lake and in the middle of the lake is an island. What will be your next move? ")
    dilemma = input("     Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
    if dilemma == "wait" or dilemma == "Wait" or dilemma == "WAIT":
        print("Down the lake you see a ferry coming to your direction and you ask for a ride.")
        print("On the island you see a room with 3 doors. Which door would you like to go in through? ")
        toughChoice = input("    Type \"Yellow\" to go in the yellow door, \"Red\" for the red door and \"Blue\" for the blue door: ")
        if toughChoice == "yellow" or toughChoice == "Yellow" or toughChoice == "YELLOW":
            print("Congratulations adventurer,here lies the treasure")
        elif toughChoice == "red" or toughChoice == "Red" or toughChoice == "RED":
            print("You tried to swim in Lava")
        elif toughChoice == "blue" or toughChoice == "Blue" or toughChoice == "BLUE":
            print("You were supper for the beasts")
        else:
            print("Tryna be smart ey. GAME OVER!!!!!!!")

    elif dilemma == "swim" or dilemma == "Swim" or dilemma == "SWIM":
        print("The lake was infested with every dangerous aquatic being in existence. GAME OVER!!!!")
    else:
        print("You tried to stray from the path and got erased from existence. GAME OVER!!!!")

elif direction == "right" or direction == "Right" or direction == "RIGHT":
    print("Oops you didn't see that hole.GAME OVER!!!!")
else:
    print("Nowhere to go chief. GAME OVER!!!!!")