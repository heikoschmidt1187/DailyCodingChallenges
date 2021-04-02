#!/bin/python3
"""
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you
can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the
minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down,
and right. You cannot move through walls. You cannot wrap around the edges of
the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
number of steps required to reach the end is 7, since we would need to go
through (1, 2) because there is a wall everywhere else on the second row.
"""
from collections import deque

def tile_walkable(board, row, col):
    M = len(board)
    N = len(board[0])

    # check top and bottom edges
    if row < 0 or row >= M:
        return False

    # check left and right edges
    if col < 0 or col >= N:
        return False
    
    # position lies inside the board, so check if there is a wall or not
    return not board[row][col]
    
def get_neighbors(board, row, col):
    # we have four directions to walk, so check for each if it's fine to 
    # go there and return a list of cords
    
    return [(r, c) for r, c in [
        (row, col - 1),     # go left
        (row, col + 1),     # go right
        (row - 1, col),     # go down
        (row + 1, col)      # go up
    ] if tile_walkable(board, r, c)]


def get_min_steps(board, start, end):
    # idea is to use BFS to explore the board and remember the steps
    # to move to a tile
    explored = set()                # holds the positions we already checked
    frontier = deque([(start, 0)])    # holds the nodes we explore
    
    # process nodes until the queue is empty
    while frontier:
        # take next tile
        coords, count = frontier.popleft()

        # end condition - we've found the target tile
        if coords == end:
            return count

        # add the node to the explored list
        explored.add(coords)
        
        # get the neighbours that can be moved to and put them
        # into the queue
        n = get_neighbors(board, coords[0], coords[1])
        
        # put the neighbors to the frontier for later processing
        frontier.extend((ne, count+1) for ne in n if ne not in explored)

if __name__ == '__main__':
    # setup data to operate on
    f = False
    t = True

    board = [[f, f, f, f],
            [t, t, f, t],
            [f, f, f, f],
            [f, f, f, f]]
    
    start = (3, 0)
    end = (0, 0)
    
    print(get_min_steps(board, start, end))