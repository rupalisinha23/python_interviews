"""
# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

# mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]
"""


def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


def create_mine_sweeper(bombs, num_rows, num_cols):
    # all fields initialized with 0 first
    matrix = [[0 for i in range(num_cols)] for j in range(num_rows)]
    # for j in range(num_rows):
    #     for i in range(num_cols):
    #         matrix[i][j] = 0
    # print(to_string(matrix))
    for bomb in bombs:
        row_i, col_i = tuple(bomb)
        matrix[row_i][col_i] = -1
        for i in range(row_i - 1, row_i + 2):
            for j in range(col_i - 1, col_i + 2):
                if 0 <= i <= num_rows - 1 and 0 <= j <= num_cols - 1 and matrix[i][j] != -1:
                    matrix[i][j] += 1
    return matrix


def click_cell_reveal(matrix, num_rows, num_cols, click_i, click_j):
    value = matrix[click_i][click_j]
    if value == -1:
        return matrix
    if value == 0:
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                if matrix[i][j] == 0:
                    matrix[i][j] = -2
    return matrix


def click_cell_reveal2(matrix, num_rows, num_cols, click_i, click_j):
    value = matrix[click_i][click_j]
    if value == -1:
        return matrix
    if value == 0:
        import queue
        checking_queue = queue.Queue()
        checking_queue.put((click_i, click_j))
        while not checking_queue.empty():
            cur_i, cur_j = checking_queue.get()
            matrix[cur_i][cur_j] = -2
            for i in range(cur_i - 1, cur_i + 2):
                for j in range(cur_j - 1, cur_j + 2):
                    if 0 <= i <= num_rows - 1 and 0 <= j <= num_cols - 1 and matrix[i][j] == 0:
                        checking_queue.put((i, j))
    return matrix


if __name__ == '__main__':
    init_matrix = create_mine_sweeper([[0, 1], [0, 3], [1, 0], [1, 2], ], 4, 4)
    print(to_string(init_matrix))
    clicked_matrix = click_cell_reveal2(init_matrix, 4, 4, 3, 0)
    print(to_string(clicked_matrix))

