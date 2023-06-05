#!/usr/bin/python3

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for i in range(n)] for j in range(n)]
    return (board)

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)

def xout(board, row, col):
    """X out spots on a chessboard."""
    # X out all forward spots
    board[row][col+1:] = ["x"] * (len(board) - col - 1)
    # X out all backwards spots
    board[row][:col] = ["x"] * col
    # X out all spots below
    board[row+1:] = [["x"] * len(board)] * (len(board) - row - 1)
    # X out all spots above
    board[:row] = [["x"] * len(board)] * row
    # X out all spots diagonally down to the right
    for r in range(row + 1, len(board)):
        c = col + 1 + r - row
        if c < len(board):
            board[r][c] = "x"
    # X out all spots diagonally up to the left
    for r in range(row - 1, -1, -1):
        c = col - 1 - (row - r)
        if c >= 0:
            board[r][c] = "x"
    # X out all spots diagonally up to the right
    for r in range(row - 1, -1, -1):
        c = col + 1 + (row - r)
        if c < len(board):
            board[r][c] = "x"
    # X out all spots diagonally down to the left
    for r in range(row + 1, len(board)):
        c = col - 1 - (r - row)
        if c >= 0:
            board[r][c] = "x"

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle. """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            board[row][c] = "Q"
            xout(board, row, c)
            solutions = recursive_solve(board, row + 1,
                                        queens + 1, solutions)
            board[row][c] = " "

    return (solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
