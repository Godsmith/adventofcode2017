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
            self._turn_left()
            self._clean()
        else:
            self._turn_right()
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
        self._table = [list(string) for string in strings]

    def infected(self, position):
        return self._table[position[1]][position[0]] == '#'

    def infect(self, position):
        self._table[position[1]][position[0]] = '#'

    def clean(self, position):
        self._table[position[1]][position[0]] = '.'
