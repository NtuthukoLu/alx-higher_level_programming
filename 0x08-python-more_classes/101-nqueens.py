#!/usr/bin/python3
"""nqueens"""
import sys

def board_safe(chess_board, column, num):
    for i in range(0, num):
        if chess_board[i][column] == 1:
            return False
    return True

def get_n_queens(chess_board, column, num):
    if column >= num:
        return True
    for i in range(0, num):
        if board_safe(chess_board, column, num):
            chess_board[i][column] = 1
            if get_n_queens(chess_board, column + 1, num):
                return True
            chess_board[i][column] = 0
    return False

args = sys.argv

if len(args) != 2:
    exit(1)
if not args[1].isdigit():
    print("N must be a number")
    exit(1)

num = int(args[1])
if num < 4:
    print("N must be at least 4")
    exit(1)

solutions = []
board = [[0 for a in range(0, num)] for b in range(0, num)]
running = True
while running:
    sol = get_n_queens(board, 0, num)
    solutions.append(sol)
    running = False
