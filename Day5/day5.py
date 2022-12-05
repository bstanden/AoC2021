# AoC 2021
# Day 5
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 5
PUZZLE_2_TEST_RESULT = 12


def do_puzzle(input, allow_diagonal=False):
    lines = [parse_input(i) for i in input]
    intersections = set()

    while len(lines):
        line = lines.pop(0)
        if is_diagonal(line) and not allow_diagonal:
            continue

        points = get_points(line)
        for l in lines:
            if not is_diagonal(l) or allow_diagonal:
                line_intersections = set(points).intersection(get_points(l))
                intersections = intersections.union(line_intersections)

    return len(intersections)


def is_diagonal(line):
    ((start_x, start_y), (end_x, end_y)) = line
    return True if (start_x != end_x) and (start_y != end_y) else False


def get_points(line):
    ((start_x, start_y), (end_x, end_y)) = line
    if start_x == end_x:
        if end_y > start_y:
            points = [(start_x, y) for y in range(start_y, end_y + 1)]
        else:
            points = [(start_x, y) for y in range(start_y, end_y - 1, -1)]
    elif end_y == start_y:
        if end_x > start_x:
            points = [(x, start_y) for x in range(start_x, end_x + 1)]
        else:
            points = [(x, start_y) for x in range(start_x, end_x - 1, -1)]
    elif start_x < end_x:
        if end_y > start_y:
            points = [(start_x + idx, y) for (idx, y) in enumerate(range(start_y, end_y + 1))]
        else:
            points = [(start_x + idx, y) for (idx, y) in enumerate(range(start_y, end_y - 1, -1))]
    else:
        if end_y > start_y:
            points = [(start_x - idx, y) for (idx, y) in enumerate(range(start_y, end_y + 1))]
        else:
            points = [(start_x - idx, y) for (idx, y) in enumerate(range(start_y, end_y - 1, -1))]

    return points


def parse_input(i):
    (start, end) = i.split('>')
    return (parse_coord(start), parse_coord(end))


def parse_coord(coord):
    (x, y) = tuple((''.join(c for c in coord if c not in '()- ')).split(','))
    return (int(x), int(y))


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    assert (do_puzzle(read_file(INPUT_FILE_TEST)) == PUZZLE_1_TEST_RESULT)

    # puzzle 1
    result = do_puzzle(read_file(INPUT_FILE))
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    assert (do_puzzle(read_file(INPUT_FILE_TEST), True) == PUZZLE_2_TEST_RESULT)

    # puzzle 2
    result = do_puzzle(read_file(INPUT_FILE), True)
    print(f"puzzle2 result: {result}")
