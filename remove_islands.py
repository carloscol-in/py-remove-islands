"""Remove islands from 2D matrix."""

# Dependencies
from typing import List

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

expected_output = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]


def remove_islands(matrix) -> List[List]:
    """
    1 -> black
    0 -> white

    Remove all islands from 2D array."""
    graph = {}

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == 1:
                graph.setdefault((row, col), get_neighbors((row, col), matrix))


def get_neighbors(rc_tup, matrix) -> List:
    """Get the neighbors horizontal and vertical for a
    point specified in the row-column tuple; rc_tup."""
    h_offset = [1, 0, -1, 0]
    v_offset = [0, 1, 0, -1]

    row, col = rc_tup

    if matrix[row][col] == 0:
        return

    return [(row + v_offset[i], col + h_offset[i]) for i in range(0, len(h_offset)) if matrix[row + v_offset[i]][col + h_offset[i]] == 1]


def get_edges(matrix) -> List:
    """Get the edge values."""
    edges = []
    for i in range(0, len(matrix)):
        for j in [0, len(matrix[i]) - 1]:
            if matrix[i][j] == 1:
                edges.append((i, j))

    for i in [0, len(matrix) - 1]:
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 1:
                if (i, j) not in edges:
                    edges.append((i, j))

    return edges
