# AoC 2021
# Day n
#
# Dr Bob, Tech Team, DigitalUK

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 40
PUZZLE_2_TEST_RESULT = 315

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

def do_puzzle1(_input):
    size=len(_input) * len(_input[0])
    graph = [[0] * size for _ in range(size)]
    for row,line in enumerate(_input):
        for col,risk in enumerate(line):
            for d in [(-1,0),(0,-1),(1,0),(0,1)]:
                dr,dc=d
                if 0 <= row+dr < len(_input) and 0 <= col+dc < len(_input[0]):
                    source=row*len(_input)+col
                    dest=(row+dr)*len(_input)+(col+dc)
                    graph[source][dest]=_input[row+dr][col+dc]

    gr = csr_matrix(graph)
    dist_matrix, predecessors = dijkstra(csgraph=gr, directed=True, indices=0, return_predecessors=True)
    return( dist_matrix[-1])

def do_puzzle(_input): # too simple
    for row in range(len(_input)):
        for col in range(len(_input[0])):
            if row == 0 and col >1:  # first row - add value of cell to left
                _input[row][col] += _input[row][col - 1]
            elif col == 0 and row >1:  # first column - add value of cell above
                _input[row][col] += _input[row - 1][col]
            elif col > 0 and row > 0:  # else add least of above or left cell
                _input[row][col] += min(_input[row - 1][col], _input[row][col - 1])
    return _input[-1][-1]


def do_puzzle2(_input):
    fullmap = [[0] * (len(_input[0])*5) for _ in range(len(_input)*5)]
    for row in range(len(_input)):
        for col in range(len(_input[0])):
            for dr in range(5):
                for dc in range(5):
                    fullmap[row+(len(_input)*dr)][col+(len(_input[0])*dc)]=((_input[row][col]+dc+dr-1)%9)+1

    return do_puzzle1(fullmap)


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
