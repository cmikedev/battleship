# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

difficulty_level = {"a": [6, 20], "b": [8, 36], "c": [10, 50]}


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

