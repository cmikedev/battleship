import os
from time import sleep
from random import randint

difficulty_level = {
    "a": [4, 2, 12], "b": [6, 4, 20],
    "c": [8, 8, 36], "d": [9, 12, 40]
    }
letters_legend = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
    "F": 5, "G": 6, "H": 7, "I": 8, "J": 9
    }
letters_used = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
line_break = "\n" + str("-" * 80) + "\n"
enemy_ships = 0


def title():
    """
    Reprints the title after each clear screen
    """
    print("<====>  BATTLESHIP!  <====>\n")
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
        "Enemy forces have invaded our waters!!!\n",
        "The enemy forces are equipped with the latest " +
        "cloaking technology making them \ninvisible to our radars. " +
        "Luckily our gunnar engineers are able to draw up " +
        "grid \nmaps on the fly to assist us in aiming our shells. " +
        "As the gunnar who has won on \nmore scratch cards than any " +
        "other you have been chosen to fire blindly into the \nsea " +
        "and hopefully destroy the enemy fleet.",
        "\nCongratulations!\n"
    ]
    title()
    print("\nIncoming message from Fleet Command......\n")
    sleep(2)
    for i in intro:
        print(i)
    continue_key()


def instructions():
    """
    This functions provides instructions to the user on playing the game
    """

    instructions_list = [
        "You must input two coordinates, a number and a letter " +
        "in order to select the \ngrid you want to fire upon:",
        "\n1. Select the grid ROW which will appear as a NUMBER",
        "2. Select the grid COLUMN which will appear as a LETTER\n",
        "* If a ship is within the grid coordinates you selected, " +
        "a hit will be \n  registered",
        "* If the grid is empty, it will be registered as a miss",
        "* The size of the grid and the amount of shells you have " +
        "will be determined by \n  the difficulty level you choose"
    ]
    title()
    print("Here is what you must do to defeat the invaders:")
    sleep(2)
    print(line_break)
    for i in instructions_list:
        print(i)
    print(line_break)
    sleep(2)
    print("Are you ready? (don't worry we'll show " +
          "you the instructions again)\n")
    continue_key()


def difficulty():
    """
    This function allows the user to select the difficulty level
    """
    global difficulty_chosen
    global grid_size
    global invaders
    global missiles

    difficulty_levels = ["a", "b", "c", "d"]
    difficulty_explanation = [
        "\n** EASY **:\nA 4x4 grid with 2 enemy ships. " +
        "You will have 12 missiles to defeat them.",
        "\n** MEDIUM **:\nA 6x6 grid with 4 enemy ships. " +
        "You will have 20 missiles to defeat them.",
        "\n** HARD **:\nA 8x8 grid with 8 enemy ships. " +
        "You will have 36 missiles to defeat them.",
        "\n** INSANE **:\nA 9x9 grid with 12 enemy ships. " +
        "You will have 40 missiles to defeat them."
    ]
    title()
    print("Now select your preferred difficulty level. " +
          "You have 4 choices:")
    sleep(2)
    for i in difficulty_explanation:
        print(i)
    print("")
    while True:
        select_difficulty = input("Please select difficulty by " +
                                  "entering 'a', 'b', 'c' or 'd': " +
                                  "\n\n a: Easy \n " +
                                  "b: Medium \n c: Hard \n d: Insane \n")
        if select_difficulty.lower() in difficulty_levels:
            difficulty_chosen = select_difficulty
            grid_size = difficulty_level[difficulty_chosen][0]
            invaders = difficulty_level[difficulty_chosen][1]
            missiles = difficulty_level[difficulty_chosen][2]
            return difficulty_chosen
        else:
            print("Invalid choice! Please select the difficulty " +
                  "by entering 'a', 'b', 'c' or 'd'")


def create_board(board):
    """
    Creates the board with the grid-size determined by the difficulty level
    """
    clear_screen()
    title()

    header = ["   "]
    for i in range(grid_size):
        header.append(letters_used[i] + "  ")
    print("** Instructions **\n")
    print("1. Select the grid ROW which will appear as a NUMBER")
    print("2. Select the grid COLUMN which will appear as a LETTER\n")
    print(*header)

    if grid_size == 4:
        print("  " + ("_" * 17))
    elif grid_size == 6:
        print("  " + ("_" * 25))
    elif grid_size == 8:
        print("  " + ("_" * 32))
    else:
        print("  " + ("_" * 37))

    # Lines 172 - 175 taken from lines 11 - 14 of gbrough Battleship.
    # See README.md Credits
    row_num = 1
    for row in board:
        print("%d | %s |" % (row_num, " | ".join(row)))
        row_num += 1
    print("")
    print(f"Enemy Ships Destroyed: {str(enemy_ships)} / {str(invaders)}")
    if missiles <= 5:
        print(f"!!LOW AMMO WARNING!! Missiles Remaining: {str(missiles)}")
    else:
        print(f"Missiles Remaining: {str(missiles)}")
    print("")


def create_ships(board):
    """
    This function creates the invading ships
    """
    # Lines 191 - 197 amended from lines 27 - 32 of gbrough Battleship.
    # See README.md Credits
    for ship in range(invaders):
        ship_row = randint(0, grid_size - 1)
        ship_column = randint(0, grid_size - 1)
        while board[ship_row][ship_column] == "X":
            ship_row = randint(0, grid_size - 1)
            ship_column = randint(0, grid_size - 1)
        board[ship_row][ship_column] = "X"


def ship_location():
    """
    This function lets the user input their guess of the enemy ship location
    """
    rows = [i + 1 for i in range(0, grid_size)]
    rows_string = "".join(map(str, rows))
    columns = letters_used[0: grid_size]
    columns_string = "".join(map(str, columns))

    while True:
        row_choice = input(f"Please enter a ship row 1-{grid_size}: ")
        if len(row_choice) == 0:
            print("Please enter a valid row")
        elif row_choice in rows_string:
            break
        else:
            print("Please enter a valid row")

    while True:
        column_choice = input(
            f"Please enter a column A-{letters_used[grid_size - 1]}: ").upper(
            )
        if len(column_choice) == 0:
            print("Please enter a valid column")
        elif column_choice in columns_string:
            break
        else:
            print("Please enter a valid column")

    return int(row_choice) - 1, letters_legend[column_choice]


def ship_hits(board):
    """
    This counts the number of ships that were hit
    """
    # lines 238 - 243 taken from lines 46 - 52 of gbrough Battleship.
    # See README.md Credits
    hits = 0
    for row in board:
        for column in row:
            if column == "X":
                hits += 1
    return hits


def play_game():
    """
    This runs the game logic
    """
    global enemy_ship_board
    global player_guess_board
    global missiles
    global enemy_ships

    def game_lost():
        """
        This displays the game over screen
        """
        clear_screen()
        title()
        print("\nMissiles out! We're defenceless!\n")
        print("\n<====>  GAME OVER!   <====>\n")

    def game_won():
        """
        This displays the won game screen
        """
        clear_screen()
        title()
        print("\nYou have sunk the invading fleet!\n")
        print("\n<====>    VICTORY!   <====>\n")

    def second_board(size):
        """
        This function is used to create the enemy and player guess boards
        """
        board_specs = []
        for i in range(size):
            board_specs.append(([" "] * size))
        return board_specs

    enemy_board = second_board(grid_size)
    player_guess_board = second_board(grid_size)

    # Lines 287 - 313 amended from lines 55 - 76 of gbrough Battleship.
    # See README.md Credits
    create_ships(enemy_board)
    while missiles > 0:
        create_board(player_guess_board)
        row, column = ship_location()
        if player_guess_board[row][column] == "-":
            print("\nYou already hit that empty piece of water!\n")
            sleep(3)
        elif enemy_board[row][column] == "X":
            print("\n<====>  DIRECT HIT!  <====>\n")
            print("\nYou hit one of their battleships!\n")
            invaders_remaining = invaders - 1 - ship_hits(player_guess_board)
            print("Enemy ships remaining: " + str(invaders_remaining))
            sleep(3)
            player_guess_board[row][column] = "X"
            missiles -= 1
            enemy_ships += 1
        else:
            print("\nYou missed!")
            sleep(3)
            player_guess_board[row][column] = "-"
            missiles -= 1
        if ship_hits(player_guess_board) == invaders:
            game_won()
            break
        if missiles == 0:
            game_lost()
            break


def main():
    """
    Runs all program functions
    """
    introduction()
    instructions()
    difficulty()
    play_game()

main()
