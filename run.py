# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
from time import sleep
import random

difficulty_level = {"a": [6, 20], "b": [8, 36], "c": [10, 45]}
board = []
grid_size = 0


def difficulty():
    """
    This function allows the user to select the difficulty level
    """
    difficulty_levels = ["a", "b", "c"]
    while True:
        select_difficulty = input("Please select difficulty by entering 'a', 'b' or 'c': \n a: Easy \n b: Medium \n c: Hard \n")
        if select_difficulty.lower() in difficulty_levels:
            return select_difficulty
        else:
            print("Invalid choice! Please select the difficulty by entering 'a', 'b' or 'c'")
        

def create_board(board):
    """
    Creates the board with the grid-size determined by the difficulty level
    """
    grid_size = difficulty_level[difficulty()][0]
    for i in range(grid_size):
        board.append(["0"] * grid_size)
    for row in board:
        print((" ").join(row))


def create_ships():
    """
    This function creates the invading ship dimensions
    """
    ship_length = random.randint(2, grid_size)
    ship_orientation = random.randint(0, 1)


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
    difficulty()

    continue_key()


def main():
    """
    Run all program functions
    """