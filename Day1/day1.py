# AoC 2021
# Day 1
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 7
PUZZLE_2_TEST_RESULT = 5


def do_puzzle1(input):
    diffs = [int(input[n]) - int(input[n - 1]) for n in range(1, len(input))]
    return sum((x > 0) for x in diffs)


def do_puzzle2(input):
    return do_puzzle1([int(input[n]) + int(input[n - 1]) + int(input[n - 2]) for n in range(2, len(input))])


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
