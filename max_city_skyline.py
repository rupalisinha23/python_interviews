def maxIncreaseKeepingSkyline(grid):
    """
    In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.
    At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
    What is the maximum total sum that the height of the buildings can be increased?
    Example:
    Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    Output: 35
    Explanation:
    The grid is:
    [ [3, 0, 8, 4],
      [2, 4, 5, 7],
      [9, 2, 6, 3],
      [0, 3, 1, 0] ]
    The skyline viewed from top or bottom is: [9, 4, 8, 7]
    The skyline viewed from left or right is: [8, 7, 9, 3]
    The grid after increasing the height of buildings without affecting skylines is:
    gridNew = [ [8, 4, 8, 7],
                [7, 4, 7, 7],
                [9, 4, 8, 7],
                [3, 3, 3, 3] ]

    :param grid:
    :return:
    """
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