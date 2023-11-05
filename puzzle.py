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


def validate_board(board: list[str]) -> bool:
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
