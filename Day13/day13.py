# AoC 2021
# Day 13
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 17


def do_puzzle1(input):
    (matrix, instructions) = parse_input(input)
    matrix = do_fold(matrix, instructions[0])
    return len(matrix)


def do_fold(matrix, i):
    new_matrix = set()
    axis, pos = i
    if (axis == 'x'):
        for p in matrix:
            (x, y) = p
            if x < pos:
                x = pos - 1 - x
                new_matrix.add((x, y))
            elif x > pos:
                x = x - pos - 1
                new_matrix.add((x, y))
    else:
        for p in matrix:
            (x, y) = p
            if y < pos:
                y = pos - 1 - y
                new_matrix.add((x, y))
            elif y > pos:
                y = y - pos - 1
                new_matrix.add((x, y))

    return new_matrix


def parse_input(input):
    matrix = set()
    instructions = []
    for i in input:
        if i.find("=") != -1:
            fold = i.split()[2]
            axis, pos = fold.split("=")
            instructions.append((axis, int(pos)))
        elif i.find(",") != -1:
            x, y = i.split(",")
            matrix.add((int(x), int(y)))
    return (matrix, instructions)


def do_puzzle2(input):
    (matrix, instructions) = parse_input(input)
    for i in instructions:
        matrix = do_fold(matrix, i)

    max_x = max([x for (x, y) in matrix])
    max_y = max([y for (x, y) in matrix])

    for y in reversed(range(max_y + 1)):
        for x in reversed(range(max_x + 1)):
            print("█" if (x, y) in matrix else " ", end='')
        print("")


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    result = do_puzzle1(read_file(INPUT_FILE_TEST))
    assert result == PUZZLE_1_TEST_RESULT, f"Failed Puzzle 1 assertion: expected {PUZZLE_1_TEST_RESULT}, got {result}"

    # puzzle 1
    result = do_puzzle1(read_file(INPUT_FILE))
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    print("puzzle2 test:")
    do_puzzle2(read_file(INPUT_FILE_TEST))

    # puzzle 2
    print("puzzle2 result:")
    do_puzzle2(read_file(INPUT_FILE))
