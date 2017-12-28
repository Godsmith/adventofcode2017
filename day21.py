from itertools import product
from math import sqrt

from util import input_rows


class Square:
    def __init__(self, rows):
        self.rows = rows

    def __eq__(self, other):
        return self.rows == other.rows

    def __repr__(self):
        return '/'.join(self.rows)

    def __str__(self):
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

    @classmethod
    def combine(cls, squares):
        child_squares_per_row = int(sqrt(len(squares)))
        child_square_size = len(squares[0].rows[0])
        rows = []
        for square_row in [squares[i:i + child_squares_per_row] for i in range(
                0, len(squares), child_squares_per_row)]:
            for row in range(child_square_size):
                rows.append(''.join(square.rows[row] for square in square_row))
        return cls(rows)

    def _iterate(self, book):
        return self.combine([square._enhance(book) for square in
                             self.break_up()])

    def _count_pixels_on(self):
        return sum(row.count('#') for row in self.rows)

    def _square_at_position(self, size, row, column):
        return [self.rows[row + i][column:column + size] for i in range(size)]

    def _size_of_child_squares(self):
        return 2 if len(self.rows) % 2 == 0 else 3

    def _iterator_over_child_square_coordinates(self):
        return self._iterate_with_step_size(self._size_of_child_squares())

    def _iterate_with_step_size(self, size):
        return product(range(0, len(self.rows), size),
                       range(0, len(self.rows), size))

    def _rotate(self):
        return Square([''.join(column) for column in zip(*reversed(self.rows))])

    def _rotations(self):
        rotate1 = self._rotate()
        rotate2 = rotate1._rotate()
        rotate3 = rotate2._rotate()
        return {self, rotate1, rotate2, rotate3}

    def _enhance(self, book):
        rotations = self._rotations()
        for key in book:
            if key in rotations:
                return book[key]
        raise ValueError(f'None of squares in {rotations} found in book!')


class EnhancementBook:
    def __init__(self, translations):
        self._translations = translations

    def __getitem__(self, item):
        return self._translations[item]

    def __iter__(self):
        return iter(self._translations)

    @classmethod
    def from_strings(cls, strings):
        dict_ = {}
        for string in strings:
            source, _, target = string.split()
            source_square = Square.from_string(source)
            target_square = Square.from_string(target)
            for rotated_source_square in source_square._rotations():
                dict_[rotated_source_square] = target_square
        return EnhancementBook(dict_)


if __name__ == '__main__':
    book = EnhancementBook.from_strings(input_rows(21))
    square = Square.from_string('.#./..#/###')
    for _ in range(5):
        square = square._iterate(book)
    print(square._count_pixels_on())
