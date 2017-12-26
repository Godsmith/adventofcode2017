from itertools import product
from math import sqrt


class Square:
    def __init__(self, rows):
        self.rows = rows

    def __eq__(self, other):
        return self.rows == other.rows

    def __repr__(self):
        return '/'.join(self.rows)

    def __hash__(self):
        return hash(''.join(self.rows))

    @classmethod
    def from_string(cls, s):
        return Square(s.split('/'))

    def break_up(self):
        return [Square(self._square_at_position(
            self._size_of_child_squares(), row, column))
            for row, column in self._iterator_over_child_square_coordinates()]

    def combine(self, squares):
        size = int(sqrt(len(squares)))



    def _square_at_position(self, size, row, column):
        return [self.rows[row + i][column:column + size] for i in range(size)]

    def _size_of_child_squares(self):
        return 2 if len(self.rows) % 2 == 0 else 3

    def _iterator_over_child_square_coordinates(self):
        return self._iterate_with_step_size(self._size_of_child_squares())

    def _iterate_with_step_size(self, size):
        return product(range(0, len(self.rows), size),
                       range(0, len(self.rows), size))
