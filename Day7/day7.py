# AoC 2021
# Day 7
#
# Dr Bob, Tech Team, DigitalUK


INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 37
PUZZLE_2_TEST_RESULT = 168


def do_puzzle1(input):
    result = {}
    for p in range(min(input), max(input) + 1):
        result[p] = sum([abs(i - p) for i in input])

    return result[min(result, key=result.get)]


def do_puzzle2(input):
    result = {}
    for p in range(min(input), max(input) + 1):
        result[p] = sum([((abs(i - p) + 1) * abs(i - p)) / 2 for i in input])

    return result[min(result, key=result.get)]


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        line = f.readline()
        return [int(x) for x in line.split(',')]


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
    result = do_puzzle2(read_file(INPUT_FILE_TEST))
    assert result == PUZZLE_2_TEST_RESULT, f"Failed Puzzle 2 assertion: expected {PUZZLE_2_TEST_RESULT}, got {result}"

    # puzzle 1
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
