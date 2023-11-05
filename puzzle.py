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


def validate_board(board: list[str]) -> bool:
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
