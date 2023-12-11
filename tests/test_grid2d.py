from common.grid import Grid2D
import pytest


def test_contruction():
    grid = Grid2D(3, 5, init=0)
    assert grid.rows() == 3
    assert grid.cols() == 5
    for i in range(3):
        for j in range(5):
            assert grid(i, j) == 0 

    grid = Grid2D([[1, 2, 3], [4, 5, 6]])
    assert grid.rows() == 2
    assert grid.cols() == 3
    for i in range(2):
        for j in range(3):
            assert grid(i, j) == 3 * i + j + 1

    grid = Grid2D.from_str_to_int('1 2 3\n4 5 6\n7 8 9', row_delim='\n', col_delim=' ')
    assert grid.rows() == 3
    assert grid.cols() == 3
    for i in range(3):
        for j in range(3):
            assert grid(i, j) == 3 * i + j

    grid = Grid2D.from_str('1,2,3\n4,5,6', row_delim='\n', col_delim=',')
    assert grid.rows() == 2
    assert grid.cols() == 3
    for i in range(2):
        for j in range(3):
            assert grid(i, j) == str(3 * i + j + 1)
