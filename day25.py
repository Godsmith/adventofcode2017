from collections import defaultdict

from util import input_rows


class Action:
    def __init__(self, write, move, next_state):
        self.write = int(write)
        self.move = int(move)
        self.next_state = next_state

    def __eq__(self, other):
        return (self.write == other.write and
                self.move == other.move and
                self.next_state == other.next_state)

    def __repr__(self):
        return f'Action({self.write},{self.move},{self.next_state})'


class State:
    def __init__(self, action_when_0, action_when_1):
        self.action_when_0 = action_when_0
        self.action_when_1 = action_when_1
        self.action = None
        self.tape = None
        self.current_position = None

    def set(self, tape, current_position):
        self.action = self.action_when_0 if tape[current_position] == 0 else \
            self.action_when_1
        self.tape = tape
        self.current_position = current_position

    def write(self):
        self.tape[self.current_position] = self.action.write

    @property
    def new_position(self):
        return self.current_position + self.action.move

    @property
    def next_state(self):
        return self.action.next_state

    def __eq__(self, other):
        return (self.action_when_0 == other.action_when_0 and
                self.action_when_1 == other.action_when_1)

    def __repr__(self):
        return 'State(%r,%r)' % (self.action_when_0, self.action_when_1)


class TuringMachine:
    def __init__(self, state_dict):
        self.tape = defaultdict(lambda: 0)
        self.state_dict = state_dict
        self.starting_state = 'A'

    def run(self, steps):
        state = self.state_dict[self.starting_state]
        current_position = 0
        for _ in range(steps):
            state.set(self.tape, current_position)
            state.write()
            current_position = state.new_position
            state = self.state_dict[state.next_state]

    def checksum(self):
        return sum(self.tape.values())

    def __str__(self):
        items = sorted(self.tape.items(), key=lambda x: x[0])
        return ' '.join(str(item[1]) for item in items)

    def __eq__(self, other):
        return (self.tape == other.tape and
                self.state_dict == other.state_dict)

    @classmethod
    def from_strings(cls, strings):
        state_dict = {}
        strings = iter(strings)
        while True:
            try:
                row = next(strings)
            except StopIteration:
                return cls(state_dict)
            if 'In state' in row:
                state_name = cls._string_between(row, 'In state ', ':')
                next(strings)
                action_when_0 = cls.action_from_iterator(strings)
                next(strings)
                action_when_1 = cls.action_from_iterator(strings)
                state_dict[state_name] = State(action_when_0, action_when_1)

    @classmethod
    def action_from_iterator(cls, iterator):
        write = cls._string_between(next(iterator), 'value ', '.')
        direction = cls._string_between(next(iterator), 'the ', '.')
        direction_int = -1 if direction == 'left' else 1
        next_state = cls._string_between(next(iterator), 'state ', '.')
        return Action(write, direction_int, next_state)

    @staticmethod
    def _string_between(string, before, after):
        return string.split(before)[-1].split(after)[0]


if __name__ == '__main__':
    machine = TuringMachine.from_strings(input_rows(25))
    machine.run(12368930)
    print(machine.checksum())
