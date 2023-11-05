'''
https://github.com/Hatitara/Kornetskyi-Yaroslav-lab8-task2.git
'''
def board_to_matrix(board: list[str]) -> list[list[str]]:
    '''
    list[str] -> list[list[str]]
    Returns board as a matrix.
    >>> board_to_matrix([\
"**** ****", \
"***1 ****", \
"**  3****", \
"* 4 1****", \
"     9 5 ", \
" 6  83  *", \
"3   1  **", \
"  8  2***", \
"  2  ****"])
    [\
['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], \
['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
[' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
[' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
[' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
[' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']]
    '''
    matrix = [list(row) for row in board]
    return matrix


def check_for_reps(row: list[str]) -> bool:
    '''
    list[str] -> bool
    Checks whether row is suitable for board.
    >>> check_for_reps(['*', '*', ' ', ' ', '3', '*', '*', '*', '*'])
    True
    >>> check_for_reps(['*', '*', '*', '*', ' ', '*', '*', '*', '*'])
    True
    >>> check_for_reps([' ', '6', ' ', '6', '8', '3', ' ', ' ', '*'])
    False
    '''
    for_check = [el for el in row if el not in ('*', ' ')]
    without_reps = list(set(for_check))
    return len(for_check) == len(without_reps)


def extract_columns(board: list[list[str]]) -> list[list[str]]:
    '''
    list[list[str]] -> list[list[str]]
    Returns list of columns of the board.
    >>> extract_columns([\
['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], \
['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
[' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
[' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
[' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
[' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    [\
['*', '*', '*', '*', ' ', ' ', '3', ' ', ' '], \
['*', '*', '*', ' ', ' ', '6', ' ', ' ', ' '], \
['*', '*', ' ', '4', ' ', ' ', ' ', '8', '2'], \
['*', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' '], \
[' ', ' ', '3', '1', ' ', '8', '1', ' ', ' '], \
['*', '*', '*', '*', '9', '3', ' ', '2', '*'], \
['*', '*', '*', '*', ' ', ' ', ' ', '*', '*'], \
['*', '*', '*', '*', '5', ' ', '*', '*', '*'], \
['*', '*', '*', '*', ' ', '*', '*', '*', '*']]
    '''
    return [[row[i] for row in board] for i in range(len(board))]


def extract_l_shape(board: list[list[str]]) -> list[list[str]]:
    '''
    list[list[str]] -> list[list[str]]
    Returns the list of the lists of L-shape elements
    for 9x9 board.
    >>> extract_l_shape([\
['*', '*', '*', '*', ' ', '*', '*', '*', '*'], \
['*', '*', '*', '1', ' ', '*', '*', '*', '*'], \
['*', '*', ' ', ' ', '3', '*', '*', '*', '*'], \
['*', ' ', '4', ' ', '1', '*', '*', '*', '*'], \
[' ', ' ', ' ', ' ', ' ', '9', ' ', '5', ' '], \
[' ', '6', ' ', ' ', '8', '3', ' ', ' ', '*'], \
['3', ' ', ' ', ' ', '1', ' ', ' ', '*', '*'], \
[' ', ' ', '8', ' ', ' ', '2', '*', '*', '*'], \
[' ', ' ', '2', ' ', ' ', '*', '*', '*', '*']])
    [\
[' ', ' ', '2', ' ', ' ', ' ', '3', ' ', ' '], \
[' ', '8', ' ', ' ', '2', ' ', '6', ' ', ' '], \
[' ', ' ', '1', ' ', ' ', ' ', ' ', '4', ' '], \
[' ', '8', '3', ' ', ' ', ' ', ' ', ' ', '1'], \
[' ', '9', ' ', '5', ' ', '1', '3', ' ', ' ']]
    '''
    central_pos = [(i,pos) for pos, i in enumerate(range(-1, -6, -1))]
    pos_for_l = [[cntr] + [(cntr[0], cntr[1] + i) for i in range(1,5)] + \
                 [(cntr[0] - i, cntr[1]) for i in range(1,5)] for cntr in central_pos]
    return [[board[coor[0]][coor[1]] for coor in shape] for shape in pos_for_l]


def validate_board(board: list[str]) -> bool:
    '''
    list[str] -> bool
    Returns True if board is valid for the game,
    else False. If the board is not the board for
    this game, returns None.
    >>> validate_board([\
"**** ****", \
"***1 ****", \
"**  3****", \
"* 4 1****", \
"     9 5 ", \
" 6  83  *", \
"3   1  **", \
"  8  2***", \
"  2  ****"])
    False
    >>> validate_board([\
"**** ****", \
"***1 ****", \
"**  3****", \
"* 4 1****", \
"     9 5 ", \
" 6  83  *", \
"3      **", \
"  8  2***", \
"  2  ****"])
    True
    >>> validate_board([\
"**** ****", \
"***1 ****", \
"**  3****", \
"* 4 1****", \
"     9 5 ", \
" 6  83  *", \
"3   1  **", \
"  8  2***", \
"  2  ****    "])

    >>> validate_board([])

    >>> validate_board(9)
    
    '''
    if isinstance(board, list) and len(board) == 9 and isinstance(board[0], str) \
        and all([len(row) == 9 for row in board]):
        matrix_board = board_to_matrix(board)
        lists_to_check = matrix_board + \
            extract_columns(matrix_board) + extract_l_shape(matrix_board)
        bool_list = [check_for_reps(list_) for list_ in lists_to_check]
        return all(bool_list)
    return None
