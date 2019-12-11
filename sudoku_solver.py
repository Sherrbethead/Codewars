"""
Description

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one
argument consisting of the 2D puzzle array, with the value 0 representing an
unknown square.
The Sudokus tested against your function will be "easy" (i.e. determinable;
there will be no need to assume and test possibilities on unknowns) and can be
solved with a brute-force approach.
For Sudoku rules, see the Wikipedia article.
"""


def fill(puzzle):
    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] == 0:
                return i, j
    return -1, -1


def check(puzzle, i, j, n):
    square = list()
    if all([n != puzzle[i][row] for row in range(9)]):
        if all([n != puzzle[col][j] for col in range(9)]):
            for sqr in puzzle[(i // 3) * 3:((i // 3) + 1) * 3]:
                square += sqr[(j // 3) * 3:((j // 3) + 1) * 3]
            if n not in square:
                return True
    return False


def sudoku(puzzle):
    i, j = fill(puzzle)
    if i == -1:
        return True
    for n in range(1, 10):
        if check(puzzle, i, j, n):
            puzzle[i][j] = n
            if sudoku(puzzle):
                return puzzle
            puzzle[i][j] = 0
    return False

print(sudoku([[5,3,0,0,7,0,0,0,0],    # [[5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6,0,0,1,9,5,0,0,0],    #  [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [0,9,8,0,0,0,0,6,0],    #  [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8,0,0,0,6,0,0,0,3],    #  [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4,0,0,8,0,3,0,0,1],    #  [4, 2, 6, 8, 5, 3, 7, 9, 1],
              [7,0,0,0,2,0,0,0,6],    #  [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [0,6,0,0,0,0,2,8,0],    #  [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [0,0,0,4,1,9,0,0,5],    #  [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [0,0,0,0,8,0,0,7,9]]))  #  [3, 4, 5, 2, 8, 6, 1, 7, 9]]

print(sudoku([[9,0,8,3,0,7,0,0,0],    # [[9, 6, 8, 3, 4, 7, 1, 5, 2],
              [5,2,0,0,8,0,7,0,0],    #  [5, 2, 4, 9, 8, 1, 7, 3, 6],
              [0,0,0,0,6,0,8,4,9],    #  [3, 1, 7, 2, 6, 5, 8, 4, 9],
              [0,0,0,0,3,0,0,1,5],    #  [4, 9, 6, 7, 3, 8, 2, 1, 5],
              [0,5,0,0,0,0,0,0,7],    #  [2, 5, 1, 4, 9, 6, 3, 8, 7],
              [8,0,0,5,0,2,0,9,0],    #  [8, 7, 3, 5, 1, 2, 6, 9, 4],
              [0,0,0,8,0,3,0,7,0],    #  [6, 4, 9, 8, 2, 3, 5, 7, 1],
              [0,0,2,0,5,4,0,0,8],    #  [7, 3, 2, 1, 5, 4, 9, 6, 8],
              [1,8,0,0,0,0,4,0,0]]))  #  [1, 8, 5, 6, 7, 9, 4, 2, 3]]
