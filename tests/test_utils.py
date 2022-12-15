from common.utils import *
import pytest


lists = [
    [1, 3, 5, 2, 4, -2, 6],
    ['a', 'c', 'B', 'Y', 'z'],
]

@pytest.mark.parametrize(
    'n, iterable, key, result',
    [
        (3, lists[0], None, [6, 5, 4]),
        (7, lists[0], None, [6, 5, 4, 3, 2, 1, -2]),
        (2, lists[1], str.lower, ['z', 'Y'])
    ],
)
def test_nlargest(n, iterable, key, result):
    assert nlargest(n, iterable, key) == result

@pytest.mark.parametrize(
    'n, iterable, key, result',
    [
        (3, lists[0], None, [-2, 1, 2]),
        (7, lists[0], None, [-2, 1, 2, 3, 4, 5, 6]),
        (2, lists[1], str.lower, ['a', 'B'])
    ]
)
def test_nsmallest(n, iterable, key, result):
    assert nsmallest(n, iterable, key) == result

@pytest.mark.parametrize(
   'a, b, result',
   [
        (range(5), range(1,6), 5),
        (range(-1, 4), range(5, 0, -1), 14),
        (range(10), range(10), 0)
   ]
)
def test_manhattan_dist(a, b, result):
    assert manhattan_dist(a, b) == result

@pytest.mark.parametrize(
    'intervals, result',
    [
        ([[3,5], [1, 3], [6,7]], 2),
        ([[11,15], [6,10], [1, 5]], 3),
        ([[-1,10], [5,9], [0,7]], 1),
        ([], 0)

    ]
)
def test_merge_intervals(intervals, result):
    assert len(merge_intervals(intervals)) == result
