from enum import Enum
from itertools import product


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __repr__(self):
        return 'Position(%s, %s)' % (self.x, self.y)


class Direction(Enum):
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4


class Step:
    def __init__(self, direction):
        RIGHT, UP, LEFT, DOWN = Direction.RIGHT, Direction.UP, \
                                Direction.LEFT, Direction.DOWN
        self.direction = direction
        self._x = {RIGHT: 1, UP: 0, LEFT: -1, DOWN: 0}
        self._y = {RIGHT: 0, UP: -1, LEFT: 0, DOWN: 1}
        self._next_direction = {RIGHT: UP, UP: LEFT, LEFT: DOWN, DOWN: RIGHT}

    @property
    def x(self):
        return self._x[self.direction]

    @property
    def y(self):
        return self._y[self.direction]

    def turn(self):
        self.direction = self._next_direction[self.direction]

    def __repr__(self):
        return 'Step(%s)' % self.direction


class SpiralSquare:
    def __init__(self, side):
        self._side = side
        self._values = {}
        self.largest_x = self.largest_y = self.smallest_x = self.smallest_y = 0

    @property
    def table(self):
        position = Position(0, 0)
        step = Step(Direction.RIGHT)
        index = 1
        while self.largest_x - self.smallest_x < self._side:
            self._values[(position.x, position.y)] = self._square_value(index,
                                                                        position)
            position += step
            index += 1
            if self._at_edge(position):
                step.turn()
        return self._create_table()

    def _at_edge(self, position):
        old_edges = self._edges
        self.largest_x = max(self.largest_x, position.x)
        self.largest_y = max(self.largest_y, position.y)
        self.smallest_x = min(self.smallest_x, position.x)
        self.smallest_y = min(self.smallest_y, position.y)
        return self._edges != old_edges

    @property
    def _edges(self):
        return (self.largest_x, self.largest_y,
                self.smallest_x, self.smallest_y)

    def _create_table(self):
        output = [[None] * self._side for _ in range(self._side)]
        x_offset = -min(self._values.keys(), key=lambda p: p[0])[0]
        y_offset = -min(self._values.keys(), key=lambda p: p[1])[1]
        for x, y in self._values.keys():
            new_x = x_offset + x
            new_y = y_offset + y
            output[new_y][new_x] = self._values[(x, y)]
        return output

    def _square_value(self, index, position):
        raise NotImplementedError


class IndexSpiralSquare(SpiralSquare):
    def _square_value(self, index, position):
        return index


class AdjacencySpiralSquare(SpiralSquare):
    def __init__(self, side, break_value):
        super(AdjacencySpiralSquare, self).__init__(side)
        self._break_value = break_value

    def _square_value(self, index, position):
        if position.x == position.y == 0:
            return 1
        sum_ = self._sum_of_adjacent_squares(position)
        if sum_ > self._break_value:
            raise FinishedException(sum_)
        else:
            return sum_

    def _sum_of_adjacent_squares(self, position):
        x_values = range(position.x - 1, position.x + 2)
        y_values = range(position.y - 1, position.y + 2)
        return sum(self._values.get((x, y), 0) for x, y in
                   product(x_values, y_values))


class FinishedException(Exception):
    pass


def main():
    SIDE = 603  # Big enough
    VALUE = 361527
    print(distance_to_center(SIDE, VALUE))
    square = AdjacencySpiralSquare(SIDE, VALUE)
    try:
        a = square.table
    except FinishedException as e:
        print(e.args[0])


def distance_to_center(side, n):
    middle = int(side / 2 - 0.5)
    table = IndexSpiralSquare(side).table
    for x, y in product(range(side), range(side)):
        if table[x][y] == n:
            return abs(x - middle) + abs(y - middle)


if __name__ == '__main__':
    main()
