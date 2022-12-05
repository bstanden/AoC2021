# AoC 2021
# Day 8
#
# Dr Bob, Tech Team, DigitalUK

import itertools

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 26
PUZZLE_2_TEST_RESULT = 61229


def do_puzzle1(input):
    return sum([sum([True if len(o) in [2, 3, 4, 7] else False for o in i.split('|')[1].split()]) for i in input])


def do_puzzle2(input):
    permutations = list(itertools.permutations("abcdefg"))
    result = 0
    digits = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

    for i in input:
        inputs, outputs = i.split('|')
        outputs = ["".join(sorted(seg)) for seg in outputs.split()]
        for p in permutations:  # brute force transform on every possible input combination
            my_inputs = ["".join(sorted(seg)) for seg in inputs.split()]
            for idx, d in enumerate(my_inputs):
                my_inputs[idx] = do_transform(p, d)
            if (all(dig in my_inputs for dig in digits)):  # if transform matches segment pattern of digits...
                for idx, d in enumerate(outputs):  # ...perform transform on outputs and read value
                    outputs[idx] = do_transform(p, d)
                result = result + sum([digits.index(o) * (10 ** (3 - o_idx)) for o_idx, o in enumerate(outputs)])
                break
    return result


def do_transform(perm, digit):
    transform = ["abcdefg"[perm.index(chr)] for chr in digit]
    transform.sort()
    return "".join(transform)


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
    result = do_puzzle2(read_file(INPUT_FILE_TEST))
    assert result == PUZZLE_2_TEST_RESULT, f"Failed Puzzle 2 assertion: expected {PUZZLE_2_TEST_RESULT}, got {result}"

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
