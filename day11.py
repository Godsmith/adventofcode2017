from util import input_rows


def distance_from_string(s):
    position1 = Position(0, 0)
    position2 = Position(0, 0)
    distances = []
    for direction in s.split(','):
        position2 = position2.walk(direction)
        distances.append(DistanceCalculator(position1, position2).distance())
        print(f'{len(distances)}/{len(s.split(","))}')
    print(max(distances))
    return DistanceCalculator(position1, position2).distance()


class Position:
    DIRECTIONS = ['nw', 'n', 'ne', 'se', 's', 'sw']

    def __init__(self, y=0, x=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Position(y={self.y}, x={self.x})'

    def walk(self, direction):
        if 'e' in direction:
            x = self.x + 1
        elif 'w' in direction:
            x = self.x - 1
        else:
            x = self.x

        if direction == 'n':
            y = self.y - 1
        elif direction == 's':
            y = self.y + 1
        elif 'n' in direction:
            if self.x % 2 == 0:
                y = self.y
            else:
                y = self.y - 1
        else:
            if self.x % 2 == 0:
                y = self.y + 1
            else:
                y = self.y

        return Position(y, x)

    @property
    def adjacent_positions(self):
        return map(self.walk, self.DIRECTIONS)

    def manhattan_distance(self, other):
        return abs(self.y - other.y) + abs(self.x - other.x)

    def __eq__(self, other):
        return (self.y, self.x) == (other.y, other.x)

    def __hash__(self):
        return hash(f'{self.y},{self.x}')

    @classmethod
    def from_position(cls, position):
        return Position(position.y, position.x)


class DistanceCalculator:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def walk_outwards(self, dict_):
        return {direction: position.walk(direction) for
                direction, position in dict_.items()}

    def distance(self):
        pos3 = self.intersecting_position()
        return (self.straight_distance(self.pos1, pos3) +
                self.straight_distance(self.pos2, pos3))

    def straight_distance(self, pos1, pos2):
        positions = {direction: Position.from_position(pos1)
                     for direction in Position.DIRECTIONS}
        distance = 0
        while True:
            if pos2 in positions.values():
                return distance
            positions = self.walk_outwards(positions)
            distance += 1

    def intersecting_position(self):
        if self.pos1 == self.pos2:
            return self.pos1
        source_positions = {direction: Position.from_position(self.pos1)
                            for direction in Position.DIRECTIONS}
        target_positions = {direction: Position.from_position(self.pos2)
                            for direction in Position.DIRECTIONS}
        visited_positions = {self.pos1, self.pos2}
        while True:
            source_positions = self.walk_outwards(source_positions)
            for position in source_positions.values():
                if position in visited_positions:
                    return position
                visited_positions.add(position)
            target_positions = self.walk_outwards(target_positions)
            for position in target_positions.values():
                if position in visited_positions:
                    return position
                visited_positions.add(position)


if __name__ == '__main__':
    input_ = input_rows(11)[0]
    print(distance_from_string(input_))
