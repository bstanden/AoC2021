# AoC 2021
# Day n
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 26397
PUZZLE_2_TEST_RESULT = 288957


def parse_line(line):
    syntax = {
        '(': ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    error = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    expect = []
    for c in line:
        if c in syntax:
            expect.append(syntax[c])
        elif c != (expect.pop() if expect else None):
            return ([], error[c])
    return (expect, 0)


def do_puzzle1(input):
    return sum([e for (expect, e) in [parse_line(i) for i in input]])


def do_puzzle2(input):
    results = []
    expects = [reversed(expect) for (expect, e) in [parse_line(i) for i in input] if not e]
    for expect in expects:
        line_result = 0
        for c in expect: line_result = (5 * line_result) + (")]}>".index(c) + 1)
        results.append(line_result)
    return sorted(results)[int(len(results) / 2)]


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
