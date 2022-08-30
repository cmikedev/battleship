# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
from time import sleep
import random

difficulty_level = {"a": [6, 20], "b": [8, 36], "c": [10, 45]}
board = []


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
        board.append(["0"]*grid_size)
    for row in board:
        print((" ").join(row))

def create(ships):
    """
    This function creates the invading ship dimensions
    """
    pass

def start_message():
    """
    This function welcomes the player and provides instructions on how to play.
    """

    def continue_key():
        input("Press any key to continue....")
        if input != " ":
            os.system('clear')

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
    
    print("BATTLESHIP")
    sleep(3)
    os.system("clear")

    for i in intro:
        print(i)
        sleep(3)

    continue_key()
        
    print("Here is what you must do to defeat the invaders:")
    sleep(3)
    
    for j in instructions:
        print(j)
        sleep(3)


    print("Are you ready?")
    continue_key()
    print("let's go!!!")

start_message()