'''Description

Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter.
If the board is valid return 'Finished!', otherwise return 'Try again!
Sudoku rules: Complete the Sudoku puzzle so that each and every row, column, and region contains
the numbers one through nine only once.
More information about rules and how to play Sudoku: http://en.wikipedia.org/wiki/Sudoku
and http://www.sudokuessentials.com/'''


def done_or_not(board):
    sumrows = [sum(i) for i in board]
    sumcols = [sum(j) for j in zip(*board)]
    sumsqrs1 = [sum(k) for k in zip(*board[:3])]
    sumsqrs2 = [sum(k) for k in zip(*board[3:6])]
    sumsqrs3 = [sum(k) for k in zip(*board[6:])]
    sumsqrs = [sum(sumsqrs1[:3]), sum(sumsqrs1[3:6]), sum(sumsqrs1[6:]),
               sum(sumsqrs2[:3]), sum(sumsqrs2[3:6]), sum(sumsqrs2[6:]),
               sum(sumsqrs3[:3]), sum(sumsqrs3[3:6]), sum(sumsqrs3[6:])]
    if sumrows.count(45) == sumcols.count(45) == sumsqrs.count(45) == 9:
        return 'Finished!'
    else:
        return 'Try again!'

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                   [4, 9, 8, 2, 6, 1, 3, 7, 5],
                   [7, 5, 6, 3, 8, 4, 2, 1, 9],
                   [6, 4, 3, 1, 5, 8, 7, 9, 2],
                   [5, 2, 1, 7, 9, 3, 8, 4, 6],
                   [9, 8, 7, 4, 2, 6, 5, 3, 1],
                   [2, 1, 4, 9, 3, 5, 6, 8, 7],
                   [3, 6, 5, 8, 1, 7, 9, 2, 4],
                   [8, 7, 9, 6, 4, 2, 1, 5, 3]]))  # Finished!
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                   [4, 9, 8, 2, 6, 1, 3, 7, 5],
                   [7, 5, 6, 3, 8, 4, 2, 1, 9],
                   [6, 4, 3, 1, 5, 8, 7, 9, 2],
                   [5, 2, 1, 7, 9, 3, 8, 4, 6],
                   [9, 8, 7, 4, 2, 6, 5, 3, 1],
                   [2, 1, 4, 9, 3, 5, 6, 8, 7],
                   [3, 6, 5, 8, 1, 7, 9, 2, 4],
                   [8, 7, 9, 6, 4, 2, 1, 3, 5]]))  # Try again!