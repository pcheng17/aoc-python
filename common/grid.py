class Grid2D:
    def __init__(self, rows: int, cols: int, val=None):
        self._rows = rows
        self._cols = cols
        self._data = [[val for _ in range(self._rows)] for _ in range(self._cols)]

    def __init__(self, data):
        self._data = data
        self._rows = len(data)
        self._cols = len(data[0])

    @classmethod
    def from_str(cls, string: str, row_delim='\n', col_delim=None):
        if col_delim is None:
            data = [[c for c in row] for row in string.split(row_delim)] 
        else:
            data = [[c for c in row.split(col_delim)] for row in string.split(row_delim)]
        return cls(data)
    
    @classmethod
    def from_str_to_int(cls, string: str, row_delim='\n', col_delim=None):
        if col_delim is None:
            data = [[int(c) for c in row] for row in string.split(row_delim)] 
        else:
            data = [[int(c) for c in row.split(col_delim)] for row in string.split(row_delim)]
        return cls(data)
    
    def rows(self):
        return self._rows

    def cols(self):
        return self._cols

    def __call__(self, i: int, j: int):
        return self._data[i][j]

    def is_in_bounds(self, i: int, j: int):
        return 0 <= i < self._rows and 0 <= j < self._cols
    
    def find_all(self, x):
        return [(i, j) for i in range(self._rows) for j in range(self._cols) if self._data[i][j] == x]
    
    def find(self, x):
        for i in range(self._rows):
            for j in range(self._cols):
                if self._data[i][j] == x:
                    return (i, j)
        return None

    def get_row(self, i):
        return self._data[i]
    
    def get_col(self, j):
        return [row[j] for row in self._data]

    def row(self, i):
        if 0 <= i < self._rows:
            for j in range(self._cols):
                yield self._data[i][j]

    def col(self, j):
        if 0 <= j < self._cols:
            for i in range(self._rows):
                yield self._data[i][j]
        
    def __str__(self):
        return '\n'.join([''.join(row) for row in self._data])

    def __repr__(self):
        return self.__str__()
    
    