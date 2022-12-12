class Grid2D:
    def __init__(self, rows: int, cols: int, init=None) -> None:
        self._rows = rows
        self._cols = cols
        self._data = [[init for _ in range(self._rows)] for _ in range(self._cols)]

    def rows(self) -> int:
        return self._rows

    def cols(self) -> int:
        return self._cols

    def __call__(self, i: int, j: int):
        return self._data[i][j]

    def isInBounds(self, i: int, j: int):
        return 0 <= i < self._rows and 0 <= j < self._cols

