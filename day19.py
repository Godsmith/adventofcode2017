from util import input_rows


class Direction:
    coordinate_changes = {'down': (1, 0),
                          'up': (-1, 0),
                          'left': (0, -1),
                          'right': (0, 1)}

    def __init__(self, direction_string):
        self._direction_string = direction_string

    @property
    def x(self):
        return self.coordinate_changes[self._direction_string][1]

    @property
    def y(self):
        return self.coordinate_changes[self._direction_string][0]


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Position(x={self.x}, y={self.y}'

    @classmethod
    def next_in_line(cls, pos1, pos2):
        x, y = pos1.x, pos1.y
        if pos1.x < pos2.x:
            x = pos2.x + 1
        elif pos1.x > pos2.x:
            x = pos2.x - 1
        elif pos1.y < pos2.y:
            y = pos2.y + 1
        elif pos1.y > pos2.y:
            y = pos2.y - 1
        return cls(x, y)


class Packet:
    def __init__(self, diagram):
        self._diagram = diagram
        self._position, self._previous_position = self._diagram.start_positions
        self.letters = ''
        self.finished = False
        self.step_count = 0

    def __repr__(self):
        return f'Position<{self._position}>'

    def step_to_next_position(self):
        self._step(self._next_position())

    def _step(self, new_position):
        self._previous_position = self._position
        self._position = new_position
        self.step_count += 1

        if self._diagram.character(self._position).isalpha():
            self.letters += self._diagram.character(self._position)

        if self._diagram.character(self._position) == ' ':
            self.finished = True

    def _next_position(self):
        if self._diagram.character(self._position) == '+':
            for position in self._potential_next_positions():
                if self._diagram.character(position) != ' ':
                    return position
        else:
            return Position.next_in_line(self._previous_position,
                                         self._position)

    def _potential_next_positions(self):
        for direction_string in Direction.coordinate_changes:
            adjacent_position = self._position + Direction(
                direction_string)
            if not adjacent_position == self._previous_position:
                yield adjacent_position


class Diagram:
    def __init__(self, table):
        self._table = table

    def character(self, position):
        return self._table[position.y][position.x]

    @property
    def start_positions(self):
        for i, s in enumerate(self._table[0]):
            if not s == ' ':
                return Position(x=i, y=0), Position(x=i, y=-1)

    @property
    def width(self):
        return len(self._table[0])


if __name__ == '__main__':
    diagram = Diagram(input_rows(19, strip=False))
    packet = Packet(diagram)
    while not packet.finished:
        packet.step_to_next_position()
    print(packet.letters)
    print(packet.step_count)
