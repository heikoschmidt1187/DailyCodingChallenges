#!/bin/python3
"""
Conway's Game of Life takes place on an infinite two-dimensional board of square
cells. Each cell is either dead or alive, and at each tick, the following rules
apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally
adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a
starting list of live cell coordinates and the number of steps it should run for.
Once initialized, it should print out the board state at each step. Since it's an
infinite board, print out only the relevant coordinates, i.e. from the top-leftmost
live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""
import time
import os
import sys

N = 20
board = []

def pretty_print():
    os.system('clear')
    global board

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 1:
                print('*', end = ' ')
            else:
                print('.', end = ' ')
        print()
        
def evolution(board):
    global N
    next = board.copy()
    
    # check each cell
    for i in range(N):
        for j in range(N):
            
            # check neigbors alive
            sum_alive = board[(i-1)%N][(j-1)%N] + board[(i-1)%N][j] + board[(i-1)%N][(j+1)%N] + \
                        board[i][(j-1)%N] + board[i][(j+1)%N] + \
                        board[(i+1)%N][(j-1)%N] + board[(i+1)%N][j] + board[(i+1)%N][(j+1)%N]

            # update next board
            if board[i][j] == 1 and (sum_alive < 2 or sum_alive > 3):
                next[i][j] = 0
            elif board[i][j] == 0 and sum_alive == 3:
                next[i][j] = 1
                
    return next
        
def game_of_life(start_set, steps):
    global board
    global N

    # initialize board
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        board.append(row)
        
    # to the steps, use step 0 for init
    for cur_step in range(steps):
        if cur_step == 0:
            # set life cells
            for s in start_set:
                r, c = s
                board[r][c] = 1
        else:
            board = evolution(board)

        pretty_print()
        time.sleep(1)

if __name__ == '__main__':
    glider = [ (0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    game_of_life(glider, 100)