# AoC 2021
# Day 11
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 1656
PUZZLE_2_TEST_RESULT = 195


def do_increment(input):
    flash_list = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            input[y][x] += 1
            if input[y][x] > 9:
                input[y][x] = 0
                flash_list.append((y, x))
    return flash_list


def do_flash_increment(input, flash_list):
    y, x = flash_list.pop(0)
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if 0 <= y + dy < len(input) and 0 <= x + dx < len(input[0]) and not (dy == dx == 0):
                if input[y + dy][x + dx] > 0:
                    input[y + dy][x + dx] += 1
                    if input[y + dy][x + dx] > 9:
                        input[y + dy][x + dx] = 0
                        flash_list.append((y + dy, x + dx))


def do_puzzle1(input):
    flash_count = 0
    for n in range(100):
        flash_list = do_increment(input)
        while len(flash_list):
            flash_count += 1
            do_flash_increment(input, flash_list)
    return flash_count


def do_puzzle2(input):
    n = 0
    while not all([input[y][x] == 0 for y in range(len(input)) for x in range(len(input[0]))]):
        flash_list = do_increment(input)
        while len(flash_list): do_flash_increment(input, flash_list)
        n += 1
    return n


# slurp file into 2d array of ints
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [[int(c) for c in e.strip()] for e in lines]


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

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
