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
        return self._grid.is_infected(self._position)

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


class Virus2(Virus):
    def _burst(self):
        if self._is_current_node_cleaned():
            self._turn_left()
            self._weaken()
        elif self._is_current_node_weakened():
            self._infect()
        elif self._is_current_node_infected():
            self._turn_right()
            self._flag()
        elif self._is_current_node_flagged():
            self._reverse()
            self._clean()
        self._move_forward()

    def _is_current_node_cleaned(self):
        return self._grid.is_cleaned(self._position)

    def _weaken(self):
        self._grid.weaken(self._position)

    def _is_current_node_weakened(self):
        return self._grid.is_weakened(self._position)

    def _flag(self):
        self._grid.flag(self._position)

    def _is_current_node_flagged(self):
        return self._grid.is_flagged(self._position)

    def _reverse(self):
        self._direction_index = (self._direction_index + 2) % 4


class Grid:
    def __init__(self, strings):
        self._dict = defaultdict(lambda: False)
        for y, row in enumerate(strings):
            for x, character in enumerate(row):
                self._dict[(x, y)] = (character == '#')

    def is_infected(self, position):
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


class Grid2:
    def __init__(self, strings):
        self._dict = defaultdict(lambda: '.')
        for y, row in enumerate(strings):
            for x, character in enumerate(row):
                self._dict[(x, y)] = character

    def is_cleaned(self, position):
        return self._dict[position] == '.'

    def is_infected(self, position):
        return self._dict[position] == '#'

    def is_weakened(self, position):
        return self._dict[position] == 'W'

    def is_flagged(self, position):
        return self._dict[position] == 'F'

    def clean(self, position):
        self._dict[position] = '.'

    def infect(self, position):
        self._dict[position] = '#'

    def weaken(self, position):
        self._dict[position] = 'W'

    def flag(self, position):
        self._dict[position] = 'F'

    def __str__(self):
        output = []
        first_row = min(self._dict.keys(), key=lambda x: x[1])[1]
        last_row = max(self._dict.keys(), key=lambda x: x[1])[1]
        first_column = min(self._dict.keys(), key=lambda x: x[0])[0]
        last_column = max(self._dict.keys(), key=lambda x: x[0])[0]
        for y in range(first_row, last_row + 1):
            current_string = ''
            for x in range(first_column, last_column + 1):
                current_string += self._dict[(x, y)] + ' '
            output.append(current_string)
        return '\n'.join(output)


if __name__ == '__main__':
    grid = Grid(input_rows(22))
    virus = Virus(grid, (12, 12))
    for _ in range(10000):
        virus._burst()
    print(virus._infect_count)

    grid2 = Grid2(input_rows(22))
    virus2 = Virus2(grid2, (12, 12))  # Don't name classes this way, easy typo
    for _ in range(10000000):
        virus2._burst()
    print(virus2._infect_count)
