def check_board_size(size):
    try:
        X, Y = list(map(int, size.split(" ")))
    except ValueError:
        return False
    if any([Y < 1, X < 1]):
        return False
    return [X, Y]


def get_board_size():
    while True:
        sz = check_board_size(input("Enter your board dimensions: "))
        if sz:
            break
        else:
            print("Invalid")

    return sz


def check_start(str, cols, rows):
    try:
        x_i, y_i = list(map(int, str.split(" ")))
    except ValueError:
        return False
    if any([x_i < 1, x_i > cols, y_i < 1, y_i > rows]):
        return False
    return [x_i - 1, y_i - 1]


def get_start_pos():
    while True:
        ans = check_start(input("Enter the knight's starting position: "), sz[0], sz[1])
        if ans:
            break
        else:
            print("Invalid")

    return ans


def create_board(rows, cols):
    if rows * cols <= 9:
        board = [["_"] * cols for _ in range(rows)]
    elif 10 <= rows * cols < 100:
        board = [["__"] * cols for _ in range(rows)]
    else:
        board = [["___"] * cols for _ in range(rows)]

    return board


def print_board(rows, cols):
    cell_size = len(board[0][0])
    print(" " + "-" * (cols * (cell_size + 1) + 3))
    for i in range(rows - 1, -1, -1):
        print(f"{i + 1}| {' '.join(board[i])} |")
    print(" " + "-" * (cols * (cell_size + 1) + 3))
    print("   " + " ".join([" " * (cell_size - 1) + str(col + 1) for col in range(cols)]))


def move_knight(col, row):
    cell_size = len(board[0][0])
    if cell_size == 1:
        board[col][row] = 'X'
    elif cell_size == 2:
        board[col][row] = ' X'
    elif cell_size == 3:
        board[col][row] = '  X'


def knight_options(col, row):
    cell_size = len(board[0][0])
    if cell_size == 1:
        board[col][row] = 'O'
    elif cell_size == 2:
        board[col][row] = ' O'
    elif cell_size == 3:
        board[col][row] = '  O'


def get_possibilities(y, x):
    options = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
    moves = []

    for option in options:
        moves.append([(option[0] + y), option[1] + x])

    not_allowed = ['*', ' *', '  *']

    pos_moves = [x for x in moves
                 if (0 <= x[0] <= sz[1] - 1)
                 and (0 <= x[1] <= sz[0] - 1)
                 and (board[x[0]][x[1]] not in not_allowed)]

    return pos_moves


def update_board_possibilities(col, row):
    cell_size = len(board[0][0])
    pos_moves = get_possibilities(col, row)
    pos_moves = [x for x in pos_moves
                 if board[x[0]][x[1]] == '_' or board[x[0]][x[1]] == '__' or board[x[0]][x[1]] == '___']
    nums = len(pos_moves)
    if cell_size == 1:
        board[col][row] = f'{nums}'
    elif cell_size == 2:
        board[col][row] = f' {nums}'
    elif cell_size == 3:
        board[col][row] = f'  {nums}'


def get_num_possibilities(pos_moves):
    for x in pos_moves:
        update_board_possibilities(x[0], x[1])


def check_next(str, cols, rows):
    try:
        x_i, y_i = list(map(int, str.split(" ")))
    except ValueError:
        return False
    if any([x_i < 1, x_i > cols, y_i < 1, y_i > rows]):
        return False

    return [x_i - 1, y_i - 1]


def get_next_move():
    not_allowed = ['_', '__', '___', 'X', ' X', '  X', '*', ' *', '  *']

    while True:
        next = check_next(input("Enter your next move: "), sz[0], sz[1])
        if next and board[next[1]][next[0]] not in not_allowed:
            break
        else:
            print("Invalid")

    return next


def aster(curr_x, curr_y):
    cell_size = len(board[0][0])
    if cell_size == 1:
        board[curr_x][curr_y] = '*'
    elif cell_size == 2:
        board[curr_x][curr_y] = ' *'
    elif cell_size == 3:
        board[curr_x][curr_y] = '  *'


def clear_nums(board):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            ' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9',
            '  0', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9']
    cell_size = len(board[0][0])
    for i in range(len(board)):
        for j in range(len(board)):
            if cell_size == 1 and board[i][j] in nums:
                board[i][j] = '_'
            elif cell_size == 2 and board[i][j] in nums:
                board[i][j] = '__'
            elif cell_size == 3 and board[i][j] in nums:
                board[i][j] = '___'


def check_win():
    cell_size = len(board[0][0])
    cells = sz[0] * sz[1]

    sum_a = 0

    if cell_size == 1:
        sum_a = sum(x.count('*') for x in board)

    elif cell_size == 2:
        sum_a = sum(x.count(' *') for x in board)

    elif cell_size == 3:
        sum_a = sum(x.count('  *') for x in board)

    if cells == sum_a:
        print('What a great tour! Congratulations!')
        return False


if __name__ == "__main__":
    sz = get_board_size()
    ans = get_start_pos()
    board = create_board(sz[1], sz[0])
    move_knight(ans[1], ans[0])
    pos_moves = get_possibilities(ans[1], ans[0])
    get_num_possibilities(pos_moves)
    print_board(sz[1], sz[0])
    aster(ans[1], ans[0])
    # print_board(sz[1], sz[0])
    visits = 1
    while True:
        next = get_next_move()
        clear_nums(board)
        move_knight(next[1], next[0])
        pos_moves = get_possibilities(next[1], next[0])
        get_num_possibilities(pos_moves)
        print_board(sz[1], sz[0])
        aster(next[1], next[0])
        visits += 1
        result = check_win()
        if result == False:
            break
        elif len(pos_moves) == 0:
            print('No more possible moves!')
            print(f'Your knight visited {visits} squares!')
            break
        else:
            continue