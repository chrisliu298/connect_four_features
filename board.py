import numpy as np

empty_board = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
)


def get_valid_moves(board):
    return [i for i, col in enumerate(board.T) if 0 in col]


def make_move(board, move, player_number):
    new_board = board.copy()
    col = new_board.T[move]
    row = np.where(col == 0)[0][-1]
    new_board[row, move] = player_number
    return new_board


def make_random_board():
    board = empty_board.copy()
    num_moves = np.random.randint(1, 43)
    for i in range(num_moves):
        valid_moves = get_valid_moves(board)
        move = np.random.choice(valid_moves)
        board = make_move(board, move, 1 if i % 2 == 0 else 2)
    return board


print(make_random_board())
print(make_random_board())
