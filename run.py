# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
from time import sleep

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


print("Welcome to Battleship")
sleep(3)
os.system("clear")
print("Warning!!!! \nEnemy forces have invaded our waters!")
sleep(3)
print("\nThe enemy forces are equipped with the latest \ncloaking technology making them invisible to our \nradars. Luckily our gunnar engineers are able to \ndraw up grid maps on the fly to assist us \nin aiming our shells.")
sleep(3)
print("\nAs the gunnar who has won on more scratch cards than any \nother you have been chose to fire blindly into the sea. \n Congratulations!")
sleep(5)
os.system("clear")
print("Here is what you must do to defeat the invaders:")
sleep(3)
print("1. Select the grid ROW which will appear as a NUMBER")
sleep(3)
print("2. Select the grid COLUMN which will appear as a LETTER")
sleep(3)
print("Are you ready?")
input("Press any key to continue....")
if input != " ":
  os.system('clear')
print("let's go!!!")