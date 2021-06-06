
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print (board[7] + "|" + board[8] + '|' + board[9])
    print (board[4] + "|" + board[5] + '|' + board[6])
    print (board[1] + "|" + board[2] + '|' + board[3])


# Take in a player input and assign their marker as 'X' or 'O'.


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Takes in the board, marker and position assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker


# checks to see if the player has won.


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))


# Randomly decide which player goes first.

import random

def choose_first():
    playerfirst = random.randint(0,1)
    if playerfirst == 0:
        return('Player A')
    else:
        return('Player B')


# Checks if a space on the board is available.

def space_check(board, position): 
    return board[position] == ' '


# Checks if the board is full and returns a boolean value.


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# Asks for a player's next position and return the position for later use.

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Where u want bruh: (1-9)'))
        
    return position


# Asks the player if they want to play again.

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# Game

print('Welcome to Tic Tac Toe!')
while True:
    board = [' ']*10
    amark,bmark = player_input()
    turn = choose_first()
    print(turn + 'WILL GO FIRST')
    readymei = input('Are u ready? yes or no').lower().startswith('y')
    if readymei:
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player A':
            display_board(board)
            place_marker(board,amark,player_choice(board))
            if win_check(board,amark):
                display_board(board)
                print('PLAYER A WINS')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("IT'S A DRAW LMAO")
                    game_on = False 
                else:
                    turn = 'Player B'
                
        else:
            display_board(board)
            place_marker(board,bmark,player_choice(board))
            if win_check(board,bmark):
                display_board(board)
                print('PLAYER B WINS')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("IT'S A DRAW LMAO")
                    game_on = False 
                else:
                    turn = 'Player A'
    if not replay():
        break