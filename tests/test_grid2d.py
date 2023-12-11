from common.grid import Grid2D
import pytest


def test_contruction():
    grid = Grid2D.new(3, 5, 0)
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

    grid = Grid2D.from_str_to_int('1 2 3\n4 5 6\n7 8 9', '\n ')
    assert grid.rows() == 3
    assert grid.cols() == 3
    for i in range(3):
        for j in range(3):
            assert grid(i, j) == 3 * i + j + 1

    grid = Grid2D.from_str('1,2,3\n4,5,6', '\n,')
    assert grid.rows() == 2
    assert grid.cols() == 3
    for i in range(2):
        for j in range(3):
            assert grid(i, j) == str(3 * i + j + 1)
        
    grid = Grid2D.from_str('abcdef\nghijkl\nmnopqr', '\n')
    assert(grid.rows() == 3)
    assert(grid.cols() == 6)
    for i in range(3):
        for j in range(6):
            assert grid(i, j) == chr(6 * i + j + ord('a'))
        
@pytest.mark.parametrize(
    'grid, delim, char, expected',  
    [
        ('#..#\n..#.\n.#..', '\n', '#', [(0, 0), (0, 3), (1, 2), (2, 1)]),
        ('... ... ...', ' ', '#', []),
        ('#,#,#,#\n#,#,#,#', '\n,', '#', [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1,  2), (1, 3)])
    ]
)
def test_find_all(grid, delim, char, expected):
    grid = Grid2D.from_str(grid, delim)
    t = grid.find_all(char)
    assert (all(x in t for x in expected) and all(x in expected for x in t))
    