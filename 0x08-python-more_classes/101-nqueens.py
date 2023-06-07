#!/usr/bin/python3
"""
module for calculation of n-queens problem
"""


import sys
if __name__ == "__main__":
    a = []
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    a = [[i, None] for i in range(n)]

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        return y in [a[x][1] for x in range(n)]

    def reject(x, y):
        """determines whether or not to reject the solution"""
        if already_exists(y):
            return False
        for i in range(x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
        return True

    def clear_a(x):
        """clears the answers from the point of failure on"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if x == n - 1:  # accepts the solution
                    print(a)
                else:
                    nqueens(x + 1)  # moves on to next x value to continue

    # start the recursive process at x = 0
    nqueens(0)
