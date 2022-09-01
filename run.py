# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
from time import sleep
from random import randint

difficulty_level = {"a": [6, 4, 20], "b": [8, 8, 36], "c": [9, 12, 40]} # key = difficulty level, values = board squares, enemy ships, missiles
letters_legend = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}
letters_used = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

# Testing variables
#difficulty_chosen = "a"
#grid_size = 6

board = []
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
    global grid_size
    global missiles

    
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
            grid_size = difficulty_level[difficulty_chosen][0]
            missiles = difficulty_level[difficulty_chosen][2]
            #return select_difficulty
            return difficulty_chosen
        else:
            print("Invalid choice! Please select the difficulty by entering 'a', 'b' or 'c'")
        

def create_board(board):
    """
    Creates the board with the grid-size determined by the difficulty level
    """

    #global grid_size
    #grid_size = difficulty_level[difficulty()][0]
    #grid_size = difficulty_level[difficulty_chosen][0]
    #grid_size = 9
    clear_screen()
    title()

    header = ["   "]
    for i in range(grid_size):
        header.append(letters_used[i] + "  ")
    print(f"Missiles Remaining: {str(missiles)}")
    print("")
    print(*header)

    #print("      A  B  C  D  E  F")
    if grid_size == 6:
        print("  " + ("_" * 25))
    elif grid_size == 8:
        print("  " + ("_" * 32))
    else:
        print("  " + ("_" * 37))

    #for i in range(grid_size):
        #board.append([" "] * grid_size)
    row_number = 1
    for row in board:
        #print((" ").join(row))
        print("%d | %s |" % (row_number, " | ".join(row)))
        row_number += 1
    print("")

def create_ships(board):
    """
    This function creates the invading ship dimensions
    """

    global num_enemy_ships

    num_enemy_ships = difficulty_level[difficulty_chosen][0]
    for ship in range(num_enemy_ships):
        ship_row, ship_column = randint(0, grid_size + 1), randint(0, grid_size + 1)
    while board[ship_row][ship_column] == "X":
        ship_row, ship_column = randint(0, grid_size + 1), randint(0, grid_size + 1)
    board[ship_row][ship_column] = "X"

    #ship_length = random.randint(2, grid_size)
    #ship_orientation = random.randint(0, 1)

def ship_location():
    """
    This function creates the location of the enemy ships
    """

    rows = [i + 1 for i in range(0, grid_size + 1)]
    rows_string = "".join(map(str, rows))
    columns = letters_used[0: grid_size + 1]
    columns_string = "".join(map(str, columns))

    
    while True:
        row_choice = input(f"Please enter a ship row 1-{grid_size}: ")
        if row_choice in rows_string:
            break
        else:
            print("Please enter a valid row")
        
    while True:
        column_choice = input(f"Please enter a column A-{letters_used[grid_size - 1]}: ").upper()
        if column_choice in columns_string:
            break
        else:
            print("Please enter a valid column")
    
        
    return int(row_choice) - 1, letters_legend[column_choice]


def ship_hits(board):
    """
    This counts the number of ships that were hit
    """

    hits = 0
    for row in board:
        for column in row:
            if column == "X":
                hits += 1
    return hits


def play_game():
    global enemy_ship_board
    global player_guess_board
    global missiles

    enemy_board = [[" "] * grid_size for x in range(grid_size)]
    player_guess_board = [[" "] * grid_size for x in range(grid_size)]
    

    
    create_ships(enemy_board)
    while missiles > 0:
        create_board(player_guess_board)
        row, column = ship_location()
        if player_guess_board[row][column] == "-":
            print("You already hit that empty piece of water!")
        elif enemy_board[row][column] == "X":
            print("DIRECT HIT!!! You hit one of their battleships!")
            player_guess_board[row][column] = "X"
            missiles -= 1
        else:
            print("You missed!")
            player_guess_board[row][column] = "-"
            missiles -= 1
        if ship_hits(player_guess_board) == num_enemy_ships:
            print("Victory! You have sunk the invading fleet!")
            break
        print(f"You have {str(missiles)} missiles left")
        if missiles == 0:
            print("Missiles out! We're defenceless!")
            print("GAME OVER")
            break
    


def main():
    """
    Run all program functions
    """

    difficulty()
    play_game()
    
main()



