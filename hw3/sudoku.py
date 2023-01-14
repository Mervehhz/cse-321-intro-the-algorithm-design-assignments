def findNextEmptyCell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def isValid(grid, cell):
    row, col = cell
    value = grid[row][col]
    for i in range(9):
        if i != col and grid[row][i] == value:
            return False

    for j in range(9):
        if j != row and grid[j][col] == value:
            return False

    for i in range(3):
        for j in range(3):
            r = row - row % 3 + i
            c = col - col % 3 + j
            if r != row and c != col and grid[r][c] == value:
                return False
    return True

def solve(grid):
    empty_cell = findNextEmptyCell(grid)
    if empty_cell is None:
        return True

    row, col = empty_cell

    for value in range(1, 10):
        grid[row][col] = value
        if isValid(grid, empty_cell) and solve(grid):
            return True

    grid[row][col] = 0
    return False

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if solve(grid):
    print("Sudoku puzzle solved!")
else:
    print("Unable to solve Sudoku puzzle.")

for i in range(9):
    print("\n")
    for j in range(9):
        print(grid[i][j], end=" ")
print("\n")
