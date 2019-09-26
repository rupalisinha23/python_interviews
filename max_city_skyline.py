def maxIncreaseKeepingSkyline(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    max_row = []
    max_column = []

    C = [[0 for _ in range(rows)] for _ in range(rows)]

    for row in grid:
        max_row.append(max(row))

    grid_transposed = [*zip(*grid)]

    for row in grid_transposed:
        max_column.append(max(row))
    sum = 0

    for i in range(rows):
        for j in range(rows):
            C[i][j] = min(max_row[i], max_column[j])
            sum = sum + C[i][j] - grid[i][j]
    return sum


grid_ex = list()
grid_ex.append([3, 0, 8, 4])
grid_ex.append([2, 4, 5, 7])
grid_ex.append([9, 2, 6, 3])
grid_ex.append([0, 3, 1, 0])

print(maxIncreaseKeepingSkyline(grid_ex))