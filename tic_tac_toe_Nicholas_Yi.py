# Tic-tac-toe Game
# Author: Nicholas Yi
# Date: August 3, 2023
# Description: This code implements a classic game of Tic-tac-toe.

import os

# Function to print the game board
def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|") 
    print(board)

# Determining which player's turn it is (X or O)
def check_turn(turn):
    if (turn % 2 == 0):
        return 'O'
    else:
        return 'X'

# Function to check if there is a win on the current board
def check_for_win(spots):
    if ( (spots[1] == spots[2] == spots[3]) or 
        (spots[4] == spots[5] == spots[6]) or 
        (spots[7] == spots[8] == spots[9]) ):
        return True
    elif ( (spots[1] == spots[4] == spots[7]) or 
        (spots[2] == spots[5] == spots[8]) or 
        (spots[3] == spots[6] == spots[9]) ):
        return True
    elif ( (spots[1] == spots[5] == spots[9]) or 
          (spots[3] == spots[5] == spots[7])):
        return True
    else:
        return False 

# Dictionary to represent board positions
spots = {1: '1', 2: '2', 3: '3', 
         4: '4', 5: '5', 6: '6', 
         7: '7', 8: '8', 9: '9'}

# Initialize game variables
playing = True
turn = 0
prev_turn = -1
complete = False

# Main game loop
while playing:

    # Clear the terminal screen
    os.system('cls'if os.name == 'nt' else 'clear')
    
    # Display the current game board
    draw_board(spots)

    # Check for turn repeats (case where user chooses invalid spot)
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn

    # Instructions to current player
    print("Player " + str((turn%2) + 1) + "'s turn: Pick your spot or press q to quit.")
    
    # User input
    choice = input()
    
    # Check if user wants to quit the game
    if (choice == 'q'):
        playing = False

    # Check if user input is valid
    elif ( (str.isdigit(choice)) and (int(choice)) in (spots) ):
        if not spots[int(choice)] in {"X", "O"}:

            # Increment number of total turns
            turn += 1
            spots[int(choice)] = check_turn(turn)
    
    # Check if there is a win
    if check_for_win(spots):
        playing = False
        complete = True
    
    # The case for a draw
    if turn > 8:
        playing = False

# The final game board update
os.system('cls'if os.name == 'nt' else 'clear')
draw_board(spots)

# Displaying the game result
if complete:
    if check_turn(turn) == 'X':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
else:
    print("It's a draw!")
        