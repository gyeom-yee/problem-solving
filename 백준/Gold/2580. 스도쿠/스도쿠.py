import sys
def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '0':
                for num in map(str, range(1, 10)):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        # this triggers backtracking.
                        board[i][j] = '0'
                return False
    print("\n".join(map(" ".join, arr)))
    sys.exit()

def is_valid(board, row, col, num):
    # Check the given number in the row, column.
    for x in range(9):
        if board[row][x] == num:
            return False
        if board[x][col] == num:
            return False

    # Check the given number in the square
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

arr = [row.split() for row in sys.stdin.readlines()]
solve_sudoku(arr)