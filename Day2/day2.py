# AoC 2021
# Day 2
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 150
PUZZLE_2_TEST_RESULT = 900


def do_puzzle1(input):
    depth = 0
    horizontal = 0

    for command in input:
        (dir, len_str) = command.split(' ')
        length = int(len_str)
        if (dir == "up"):
            depth = depth - length
        elif (dir == "down"):
            depth = depth + length
        elif (dir == 'forward'):
            horizontal = horizontal + length

    return horizontal * depth


def do_puzzle2(input):
    depth = 0
    horizontal = 0
    aim = 0

    for command in input:
        (dir, len_str) = command.split(' ')
        length = int(len_str)
        if (dir == "up"):
            aim = aim - length
        elif (dir == "down"):
            aim = aim + length
        elif (dir == 'forward'):
            horizontal = horizontal + length
            depth = depth + (aim * length)

    return horizontal * depth


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    assert (do_puzzle1(read_file(INPUT_FILE_TEST)) == PUZZLE_1_TEST_RESULT)

    # puzzle 1
    result = do_puzzle1(read_file(INPUT_FILE))
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    assert (do_puzzle2(read_file(INPUT_FILE_TEST)) == PUZZLE_2_TEST_RESULT)

    # puzzle 1
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
