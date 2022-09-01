# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
from time import sleep
import random

difficulty_level = {"a": [6, 20], "b": [8, 36], "c": [10, 45]}
letters_legend = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}
letters_used = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
#difficulty_chosen = ""
board = []
enemy_ships = []
player_guesses = []
grid_size = 0
shots_fired = 0

def title():
    """
    Reprints the title after each clear screen
    """
    print("               <====>  BATTLESHIP!  <====>\n")
    sleep(1)

def clear_screen():
    """
    This function clears the screen based on the users operating system
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("clr")

def continue_key():
    """
    This function avoids repeating the below two commands
    """
    continue_pressed = ['c']
    while True:
        c_pressed = input("Press 'c' to and hit return continue....")
        if c_pressed.lower() in continue_pressed:
            return clear_screen()
        else:
            print("Nope, please press 'c' and hit return to continue")
    
def introduction():
    """
    This gives the user a brief background story
    """
    intro = [
        "\nWarning!!!\n",
        "\nEnemy forces have invaded our waters!!!\n",
        "\nThe enemy forces are equipped with the latest cloaking technology making them invisible to our radars.\n",
        "\nLuckily our gunnar engineers are able to draw up grid maps on the fly to assist us in aiming our shells.\n",
        "\nAs the gunnar who has won on more scratch cards than any other you have been chosen to fire blindly into the sea and hopefully destroy the enemy fleet.\n",
        "\nCongratulations!\n"
    ]
    title()
    print("\nIncoming message from Fleet Command......\n")
    sleep(4)
    for i in intro:
        print(i)
        sleep(1)
    continue_key()

def instructions():
    """
    This functions provides instructions to the user on playing the game
    """
    instructions_list = [
        "\nYou must input two coordinates, a number and a letter in order to select the grid you want to fire upon\n",
        "\n1. Select the grid ROW which will appear as a NUMBER\n",
        "\n2. Select the grid COLUMN which will appear as a LETTER\n",
        "\nIf a ship is within the grid coordinates you selected, a hit will be registered\n",
        "\nIf the grid is empty, it will be registered as a miss",
        "\nThe size of the grid and the amount of shells you have will be determined by the difficulty level you choose\n"
    ]
    title()
    print("Here is what you must do to defeat the invaders:")
    sleep(4)
    for i in instructions_list:
        print(i)
        sleep(1)
    sleep(4)
    print("\nAre you ready? (don't worry we'll show you the instructions again)\n")
    sleep(4)
    print("\nLET'S GO!!!\n")
    continue_key()

def difficulty():
    """
    This function allows the user to select the difficulty level
    """
    global difficulty_chosen
    difficulty_levels = ["a", "b", "c"]
    difficulty_explanation = [
        "\nYou must now select the difficulty level. You have 3 choices:\n",
        "\nEASY: 6x6 grid with 3 enemies of random size and 20 missiles\n",
        "\nMEDIUM: 8x8 grid with 4 enemies of random size and 36 missiles\n",
        "\nHARD: 10x10 grid with 1 enemy of 1 square with 50 missiles\n"
    ]
    for i in difficulty_explanation:
        print(i)
        sleep(1)
    while True:
        select_difficulty = input("Please select difficulty by entering 'a', 'b' or 'c': \n\n a: Easy \n b: Medium \n c: Hard \n")
        if select_difficulty.lower() in difficulty_levels:
            difficulty_chosen = select_difficulty
            #return select_difficulty
            return difficulty_chosen
        else:
            print("Invalid choice! Please select the difficulty by entering 'a', 'b' or 'c'")
        

def create_board(board):
    """
    Creates the board with the grid-size determined by the difficulty level
    """
    #grid_size = difficulty_level[difficulty()][0]
    grid_size = difficulty_level[difficulty_chosen][0]
    clear_screen()
    title()

    header = ["         "]
    for i in range(grid_size):
        header.append(letters_used[i] + "  ")
    print(*header)

    #print("      A  B  C  D  E  F")
    print("      ________________")
    for i in range(grid_size):
        board.append(["0"] * grid_size)
    row_number = 1
    for row in board:
        #print((" ").join(row))
        print("%d|%s|" % (row_number, " | ".join(row)))
        row_number += 1


def create_ships():
    """
    This function creates the invading ship dimensions
    """
    if difficulty_chosen == "a":
        enemy_ships = [[[2,2],[2,3],[2,4]],[4,4],[[5,5],[4,5],[3,5],[2,5]]]
    if difficulty_chosen == "b":
        enemy_ships = [[[7,5],[6,5],[5,5]],[[2,1],[2,2]],[[6,1],[6,2],[6,3],[6,4]],[7,7]]
    if difficulty_chosen == "c":
        ship_length = random.randint(2, grid_size)
        ship_orientation = random.randint(0, 1)
        enemy_ships = [ship_length, ship_orientation]


def start_message():
    """
    This function welcomes the player and provides instructions on how to play.
    """

    def title():
        """
        Reprints the title after each clear screen
        """
        print("               <====>  BATTLESHIP!  <====>\n")
        sleep(2)

    def clear_screen():
        """
        This function clears the screen based on the users operating system
        """
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("clr")

    def continue_key():
        """
        This function avoids repeating the below two commands
        """
        continue_pressed = ['c']
        while True:
            c_pressed = input("Press 'c' to and hit return continue....")
            if c_pressed.lower() in continue_pressed:
                return clear_screen()
            else:
                print("Nope, please press 'c' and hit return to continue")
    
    intro = [
        "Warning!!!",
        "\nEnemy forces have invaded our waters!!!\n",
        "\nThe enemy forces are equipped with the latest cloaking technology making them invisible to our radars.\n",
        "\nLuckily our gunnar engineers are able to draw up grid maps on the fly to assist us in aiming our shells.\n",
        "\nAs the gunnar who has won on more scratch cards than any other you have been chosen to fire blindly into the sea and hopefully destroy the enemy fleet.\n",
        "\nCongratulations!\n"
    ]
    
    instructions = [
        "\nYou must input two coordinates, a number and a letter in order to select the grid you want to fire upon\n",
        "\n1. Select the grid ROW which will appear as a NUMBER\n",
        "\n2. Select the grid COLUMN which will appear as a LETTER\n",
        "\nIf a ship is within the grid coordinates you selected, a hit will be registered\n",
        "\nIf the grid is empty, it will be registered as a miss",
        "\nThe size of the grid and the amount of shells you have will be determined by the difficulty level you choose\n"
    ]

    difficulty_explanation = [
        "\nYou must now select the difficulty level. You have 3 choices:\n",
        "\nEASY: 6x6 grid with 3 enemies of random size and 20 missiles\n",
        "\nMEDIUM: 8x8 grid with 4 enemies of random size and 36 missiles\n",
        "\nHARD: 10x10 grid with 1 enemy of 1 square with 50 missiles\n"
    ]
    
    title()

    for i in intro:
        print(i)
        sleep(2)

    continue_key()
    
    title()
    print("Here is what you must do to defeat the invaders:")
    sleep(2)
    
    for j in instructions:
        print(j)
        sleep(2)


    print("\nAre you ready?\n")
    print("\nLET'S GO!!!\n")
    continue_key()
    
    title()
    for k in difficulty_explanation:
        print(k)
        sleep(1)

    continue_key()


def main():
    """
    Run all program functions
    """
    create_board(board)
    create_ships()
    print(difficulty_chosen)

difficulty()
create_board(board)