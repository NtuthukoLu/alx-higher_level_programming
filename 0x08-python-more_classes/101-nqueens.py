#!/usr/bin/python3

import sys

def solve(board, col, n):
    if col >= n:
        print_board(board, n)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n)
            board[i][col] = 0

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print(i, end="")
                if j != n - 1:
                    print(", ", end="")
        if i != n - 1:
            print(", ", end="")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for i in range(n)] for j in range(n)]
    solve(board, 0, n)
