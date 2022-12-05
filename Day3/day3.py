# AoC 2021
# Day 3
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 198
PUZZLE_2_TEST_RESULT = 230


def get_gamma_epsilon(input):
    one_count = [0] * len(input[0])
    zero_count = [0] * len(input[0])

    epsilon = 0
    gamma = 0
    for line in input:
        for c in range(len(line)):
            if line[c] == "1":
                one_count[c] = one_count[c] + 1
            else:
                zero_count[c] = zero_count[c] + 1

    for c in range(len(input[0])):
        if one_count[c] > zero_count[c]:
            gamma = (gamma * 2) + 1
            epsilon = epsilon * 2
        else:
            epsilon = (epsilon * 2) + 1
            gamma = gamma * 2

    return (gamma, epsilon)


def get_lsr(input):
    return (commonest(True, input), commonest(False, input))


def commonest(state, input):
    for c in range(0, len(input[0])):
        input = [i for i in input if match_frequency(i[c], c, state, input)]
        if len(input) == 1:
            return int(input[0], 2)


def match_frequency( ch, index, state, input):
    chars=[i[index] for i in input]
    zeroes=chars.count('0')
    ones=chars.count('1')

    if state:
        if zeroes==ones:
            return True if ch=='1' else False
        else:
            return True if (ch=='1' and ones>zeroes) or (ch=='0' and ones<zeroes) else False
    else:
        if zeroes==ones:
            return True if ch=='0' else False
        else:
            return True if (ch=='1' and ones<zeroes) or (ch=='0' and ones>zeroes) else False


def do_puzzle1(input):
    (gamma, epsilon) = get_gamma_epsilon(input)
    return (gamma * epsilon)


def do_puzzle2(input):
    (ogr, co2_sr) = get_lsr(input)
    return (ogr * co2_sr)


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
