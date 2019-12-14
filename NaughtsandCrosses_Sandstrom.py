#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:21:07 2019

@author: Sandstrom
"""

# 'NAUGHTS AND CROSSES WHERE COMPUTER PLAYS YOU'

import random #This imports all the external functions we need - there is only one called Random

def THE_BOARD(space):
    # PRINTS THE CURRENT BOARD ENVIROMENT
    # STRINGS THAT MAKE UP THE BOARD ENVIROMENT 
    print('   |   |')
    print(' ' + space[1] + ' | ' + space[2] + ' | ' + space[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + space[4] + ' | ' + space[5] + ' | ' + space[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + space[7] + ' | ' + space[8] + ' | ' + space[9])
    print('   |   |')

def O_OR_X():
    # ALLOWS YOU TO CHOOSE O OR X, WHATEVER YOU CHOOSE THE COMPUTER HAS THE OTHER ONE
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def THE_FIRST_MOVE():
    # EITHER COMPUTER OR YOU GOES FIRST - THIS RANDOMLY CHOOSES WHO 
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    
def MAKE_YOUR_MOVE(board, letter, move):
    board[move] = letter

def ANOTHER_GAME():
    # ALLOWS THE PLAYER TO PLAY ANOTHER GAME IF THEY WANT AT THE END
    print('PLAY AGAIN? (yes or no)')
    return input().lower().startswith('y')


def DID_YOU_WIN(board, letter):
    #TELLS YOU THE WINNING BOARD POSITIONS
    #RETURNS TRUE IF THE PLAYER WINS
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def COPYBOARD(board):
    # DUPLICATES THE BOARD
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def PLAYERMOVE(board):
    # LETS THE PLAYER PLAY THE MOVE
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not FREESPACE(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def FREESPACE(board, move):
    # Return true if the passed move is free on the passed board
    return board[move] == ' '


def CHOOSE_YOUR_MOVE(board, movesList):
    #ONLY ALLOWS THE PLAYER TO PLAY MOVES THAT ARE AVAILABLE
    possibleMoves = []
    for i in movesList:
        if FREESPACE(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def COMPUTERS_MOVE(board, computerLetter):
    #COMPUTER CHOOSES A MOVE
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # NAUGHTS AND CROSSES COMPUTER ARTIFICIAL INTELEGENCE
    # IF NEXT MOVE CAN WIN - MAKE THAT MOVE
    for i in range(1, 10):
        copy = COPYBOARD(board)
        if FREESPACE(copy, i):
            MAKE_YOUR_MOVE(copy, computerLetter, i)
            if DID_YOU_WIN(copy, computerLetter):
                return i

    # CHECK IF PLAYER COULD WIN NEXT MOVE AND BLOCK
    for i in range(1, 10):
        copy = COPYBOARD(board)
        if FREESPACE(copy, i):
            MAKE_YOUR_MOVE(copy, playerLetter, i)
            if DID_YOU_WIN(copy, playerLetter):
                return i

    # TAKE A CORNER
    move = CHOOSE_YOUR_MOVE(board, [1, 3, 7, 9])
    if move != None:
        return move

    # TTAKE THE CENTER
    if FREESPACE(board, 5):
        return 5

    # TAKE A SIDE
    return CHOOSE_YOUR_MOVE(board, [2, 4, 6, 8])

def FULL_BOARD(board):
    # RETURN TRUE IS ALL SPACES ARE TAKEN OTHERWISE FALSE
    for i in range(1, 10):
        if FREESPACE(board, i):
            return False
    return True


print('HELLO LET US PLAY')

while True:
    # RESETS THE BOARD
    theBoard = [' '] * 10
    playerLetter, computerLetter = O_OR_X()
    turn = THE_FIRST_MOVE()
    print('THE ' + turn + ' GOES FIRST')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # THE PLAYER'S TURN
            THE_BOARD(theBoard)
            move = PLAYERMOVE(theBoard)
            MAKE_YOUR_MOVE(theBoard, playerLetter, move)

            if DID_YOU_WIN(theBoard, playerLetter):
                THE_BOARD(theBoard)
                print('VICTORY YOU WIN')
                gameIsPlaying = False
            else:
                if FULL_BOARD(theBoard):
                    THE_BOARD(theBoard)
                    print('TIE')
                    break
                else:
                    turn = 'computer'

        else:
            # THE COMPUTER'S TURN
            move = COMPUTERS_MOVE(theBoard, computerLetter)
            MAKE_YOUR_MOVE(theBoard, computerLetter, move)

            if DID_YOU_WIN(theBoard, computerLetter):
                THE_BOARD(theBoard)
                print('YOU LOSE')
                gameIsPlaying = False
            else:
                if FULL_BOARD(theBoard):
                    THE_BOARD(theBoard)
                    print('TIE')
                    break
                else:
                    turn = 'player'

    if not ANOTHER_GAME():
        break