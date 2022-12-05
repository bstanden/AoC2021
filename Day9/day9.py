# AoC 2021
# Day 9
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 15
PUZZLE_2_TEST_RESULT = 1134

from scipy.ndimage import label
import numpy as np


def do_puzzle1(input):
    result = 0
    for x in range(len(input[0])):
        for y in range(len(input)):
            neighbours = [input[y + dy][x + dx] for dy in range(-1, 2) for dx in range(-1, 2)
                          if (y + dy >= 0 and y + dy < len(input)) and (x + dx >= 0 and x + dx < len(input[y]))
                          and not (dx == dy == 0)]
            if all(input[y][x] < n for n in neighbours):
                result = result + 1 + input[y][x]
    return result


def do_puzzle2(input):
    basins, num_basins = label(np.array([[n < 9 for n in line] for line in input]))
    biggest = [sum([sum([n == size + 1 for n in line]) for line in basins]) for size in range(num_basins)]
    biggest.sort()
    return np.prod(biggest[-3:])


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
