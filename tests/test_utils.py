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
