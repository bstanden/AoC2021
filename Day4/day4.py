# AoC 2021
# Day 4
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 4512
PUZZLE_2_TEST_RESULT = 1924


def do_puzzle(input, solve_first=True):
    callout = input.pop(0).split(',')
    boards = []
    while len(input) > 5:
        input.pop(0)
        boards.append([input.pop(0).split() for x in range(0, 5)])

    for n in callout:
        for bindex, board in enumerate(boards):
            for lindex, line in enumerate(board):
                line = [x if x != n else '' for x in line]
                board[lindex] = line
            boards[bindex] = board
            if (board_solved(board)):
                if solve_first:
                    return sum_board(board) * int(n)
                else:
                    if all(board_solved(b) for b in boards):
                        return sum_board(board * int(n))

    return -1


def sum_board(board):
    return sum(sum([int(x) if x != '' else 0 for x in line]) for line in board)


def board_solved(board): # zip(*board[::-1]) ... rotate 90deg
    return True if any([all(n == '' for n in line) for line in board]) \
        or any([all(n == '' for n in line) for line in zip(*board[::-1])]) \
        else False


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    assert (do_puzzle(read_file(INPUT_FILE_TEST)) == PUZZLE_1_TEST_RESULT)

    # puzzle 1
    result = do_puzzle(read_file(INPUT_FILE))
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    assert (do_puzzle(read_file(INPUT_FILE_TEST), False) == PUZZLE_2_TEST_RESULT)

    # puzzle 2
    result = do_puzzle(read_file(INPUT_FILE), False)
    print(f"puzzle2 result: {result}")
