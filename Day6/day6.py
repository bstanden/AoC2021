# AoC 2021
# Day 6
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = {18: 26,
                        80: 5934,
                        256: 26984457539}

PUZZLE_1_INPUT = 80
PUZZLE_2_INPUT = 256


def do_puzzle(fish, days):
    fish_status = [fish.count(d) for d in range(9)]
    for d in range(days):
        fish_status.append(fish_status.pop(0))
        fish_status[6] = fish_status[6] + fish_status[8]
    return sum(fish_status)


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        line = f.readline()
        return [int(x) for x in line.split(',')]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    for (days, fish) in PUZZLE_1_TEST_RESULT.items():
        result=do_puzzle(read_file(INPUT_FILE_TEST), days)
        assert result == fish, f"Failed: expected {fish} for {days}, got {result}"

    # puzzle 1
    result = do_puzzle(read_file(INPUT_FILE), PUZZLE_1_INPUT)
    print(f"puzzle1 result: {result}")

    # puzzle 2
    result = do_puzzle(read_file(INPUT_FILE), PUZZLE_2_INPUT)
    print(f"puzzle2 result: {result}")
