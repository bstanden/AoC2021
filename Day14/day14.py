# AoC 2021
# Day 14
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 1588
PUZZLE_2_TEST_RESULT = 2188189693529


def parse_input(_input):
    output = ""
    rules = {}
    for i in _input:
        if i:
            if i.find("-") == -1:
                output = i
            else:
                sequence, separator, insert = i.split()
                rules[sequence] = {"insert": insert}
    return output, rules


def do_puzzle(_input, iterations):
    (output, rules) = parse_input(_input)
    vocabulary = set([r["insert"] for r in rules.values()])

    for r in rules:
        rules[r]["effect"] = [dict.fromkeys(vocabulary, 0)] * iterations

    for i in range(iterations):
        for r in rules:
            if i == 0:
                rules[r]["effect"][i][rules[r]["insert"]] = 1  # effect in first iteration is to add a single child char
            else:
                ra = r[0] + rules[r]["insert"]  # at subsequent iteration, add effect* of child char (two pairs)
                rb = rules[r]['insert'] + r[1]
                rules[r]['effect'][i] = rules[ra]['effect'][i - 1].copy()  # ...*NB use effect of previous iteration
                for v in rules[r]['effect'][i]:
                    rules[r]['effect'][i][v] += rules[rb]['effect'][i - 1][v]

    results = []
    for v in vocabulary:
        vocab_sums = sum([sum([rules[p]['effect'][i][v] for i in range(iterations)]) for p in
                          (output[c:c + 2] for c in range(len(output) - 1))])  # for each pair, for each char, total sum
        vocab_sums += output.count(v)  # don't forget to add chars in initial template!
        results.append(vocab_sums)

    results.sort()  # sort
    return results[-1] - results[0]  # difference between biggest and smallest


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    result = do_puzzle(read_file(INPUT_FILE_TEST), 10)
    assert result == PUZZLE_1_TEST_RESULT, f"Failed Puzzle 1 assertion: expected {PUZZLE_1_TEST_RESULT}, got {result}"

    # puzzle 1
    result = do_puzzle(read_file(INPUT_FILE), 10)
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    result = do_puzzle(read_file(INPUT_FILE_TEST), 40)
    assert result == PUZZLE_2_TEST_RESULT, f"Failed Puzzle 2 assertion: expected {PUZZLE_2_TEST_RESULT}, got {result}"

    # puzzle 2
    result = do_puzzle(read_file(INPUT_FILE), 40)
    print(f"puzzle2 result: {do_puzzle(read_file(INPUT_FILE), 100)}")

    print("For fun and robustness...")
    for i in [100, 1000, 10000]:
        print(f"{i} iterations: {do_puzzle(read_file(INPUT_FILE), i)}")
