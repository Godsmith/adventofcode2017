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


def main():
    SIDE = 603  # Big enough
    print(distance_to_center(SIDE, 361527))
    square = AdjacencySpiralSquare(SIDE)


def distance_to_center(side, n):
    middle = int(side / 2 - 0.5)
    table = SpiralSquare(side).table
    for x, y in product(range(side), range(side)):
        if table[x][y] == n:
            return abs(x - middle) + abs(y - middle)


class SpiralSquare:
    def __init__(self, side):
        largest_x = largest_y = smallest_x = smallest_y = 0
        self.values = {}
        position = Position(0, 0)
        step = Step(Direction.RIGHT)
        index = 1
        while largest_x - smallest_x < side:
            self.values[(position.x, position.y)] = self.square_value(index,
                                                                      position)
            position += step
            index += 1
            if position.x > largest_x:
                largest_x = position.x
                step.turn()
            if position.y > largest_y:
                largest_y = position.y
                step.turn()
            if position.x < smallest_x:
                smallest_x = position.x
                step.turn()
            if position.y < smallest_y:
                smallest_y = position.y
                step.turn()
        output = [[None] * side for _ in range(side)]
        x_offset = -min(self.values.keys(), key=lambda p: p[0])[0]
        y_offset = -min(self.values.keys(), key=lambda p: p[1])[1]
        for x, y in self.values.keys():
            new_x = x_offset + x
            new_y = y_offset + y
            output[new_y][new_x] = self.values[(x, y)]
        self.table = output

    def square_value(self, index, position):
        return index


class AdjacencySpiralSquare(SpiralSquare):
    def square_value(self, index, position):
        if position.x == position.y == 0:
            return 1
        x_values = range(position.x - 1, position.x + 2)
        y_values = range(position.y - 1, position.y + 2)
        sum_ = sum(self.values.get((x, y), 0) for x, y in
                   product(x_values, y_values))
        if sum_ > 361527:
            print(sum_)
            exit()
        else:
            return sum_


if __name__ == '__main__':
    main()
