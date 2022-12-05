# AoC 2021
# Day 12
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE = "input.txt"

PUZZLE_1_TESTS = {
    "input_test1.txt": 10,
    "input_test2.txt": 19,
    "input_test3.txt": 226
}

PUZZLE_2_TESTS = {
    "input_test1.txt": 36,
    "input_test2.txt": 103,
    "input_test3.txt": 3509
}


def create_map(input):
    cave_map = {}
    for i in input:
        a, b = i.split("-")
        for (x, y) in [(a, b), (b, a)]:
            if x not in cave_map:
                cave_map[x] = {y}
            else:
                cave_map[x].add(y, )
    return cave_map


def count_routes(node, cave_map):
    if node == "end":
        return 1

    my_map = dict()
    for k, v in cave_map.items():
        my_map[k] = set(v)
    if node.islower():
        for n in my_map:
            if node in my_map[n]:
                my_map[n].remove(node)
    return sum([count_routes(n, my_map) for n in cave_map[node]])


def do_puzzle1(input):
    cave_map = create_map(input)
    return count_routes("start", cave_map)


def count_routes_dup(node, cave_map, dup_cave):
    new_cave = dup_cave + "z"
    my_map = dict()
    for k, v in cave_map.items():
        my_map[k] = set(v)

    my_map[new_cave] = set(my_map[dup_cave])
    for k, v in my_map.items():
        if dup_cave in v:
            my_map[k].add(new_cave, )

    routes = []
    get_all_routes("start", my_map, routes)
    return int(len([r for r in routes if new_cave in r and dup_cave in r and "end" in r]) / 2)


def get_all_routes(node, cave_map, routes, path=[]):
    my_path = path.copy()
    my_path.append(node)
    if node == "end":
        routes.append(my_path)
        return

    my_map = dict()
    for k, v in cave_map.items():
        my_map[k] = set(v)
    if node.islower():
        for n in my_map:
            if node in my_map[n]:
                my_map[n].remove(node)

    if not cave_map[node]:
        routes.append(my_path)

    for n in cave_map[node]:
        get_all_routes(n, my_map, routes, my_path)


def do_puzzle2(input):
    cave_map = create_map(input)
    small_caves = set(n for n in cave_map.keys() if n.islower() and n != "start" and n != "end")
    return sum(count_routes_dup("start", cave_map, c) for c in small_caves) + count_routes("start", cave_map)


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    for (test_file, test_result) in PUZZLE_1_TESTS.items():
        result = do_puzzle1(read_file(test_file))
        print(f"Puzzle 1 assertion in {test_file}: expected {test_result}, got {result}")
        assert result == test_result, f"Failed Puzzle 1 assertion in {test_file}: expected {test_result}, got {result}"

    # puzzle 1
    result = do_puzzle1(read_file(INPUT_FILE))
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    for (test_file, test_result) in PUZZLE_2_TESTS.items():
        result = do_puzzle2(read_file(test_file))
        print(f"Puzzle 2 assertion in {test_file}: expected {test_result}, got {result}")
        assert result == test_result, f"Failed Puzzle 2 assertion in {test_file}: expected {test_result}, got {result}"

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
