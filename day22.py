from collections import defaultdict

from util import input_rows


class Virus:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

    def __init__(self, grid, starting_position):
        self._grid = grid
        self._position = starting_position
        self._direction_index = 0
        self._infect_count = 0

    def _burst(self):
        if self._is_current_node_infected():
            self._turn_right()
            self._clean()
        else:
            self._turn_left()
            self._infect()
        self._move_forward()

    def _turn_left(self):
        self._direction_index = (self._direction_index - 1) % 4

    def _turn_right(self):
        self._direction_index = (self._direction_index + 1) % 4

    def _infect(self):
        self._grid.infect(self._position)
        self._infect_count += 1

    def _clean(self):
        self._grid.clean(self._position)

    def _is_current_node_infected(self):
        return self._grid.infected(self._position)

    def _move_forward(self):
        x, y = self._position
        direction = self.DIRECTIONS[self._direction_index]
        if direction == self.UP:
            y -= 1
        if direction == self.DOWN:
            y += 1
        if direction == self.LEFT:
            x -= 1
        if direction == self.RIGHT:
            x += 1
        self._position = (x, y)


class Grid:
    def __init__(self, strings):
        self._dict = defaultdict(lambda: False)
        for y, row in enumerate(strings):
            for x, character in enumerate(row):
                self._dict[(x, y)] = (character == '#')

    def infected(self, position):
        return self._dict[position]

    def infect(self, position):
        self._dict[position] = True

    def clean(self, position):
        self._dict[position] = False

    def __str__(self):
        output = []
        first_row = min(self._dict.keys(), key=lambda x: x[1])[1]
        last_row = max(self._dict.keys(), key=lambda x: x[1])[1]
        first_column = min(self._dict.keys(), key=lambda x: x[0])[0]
        last_column = max(self._dict.keys(), key=lambda x: x[0])[0]
        for y in range(first_row, last_row + 1):
            current_string = ''
            for x in range(first_column, last_column + 1):
                if self._dict[(x, y)]:
                    current_string += '# '
                else:
                    current_string += '. '
            output.append(current_string)
        return '\n'.join(output)


if __name__ == '__main__':
    grid = Grid(input_rows(22))
    virus = Virus(grid, (12, 12))
    for _ in range(10000):
        virus._burst()
    print(virus._infect_count)
