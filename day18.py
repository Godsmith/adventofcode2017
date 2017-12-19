from collections import defaultdict

from util import input_lists


class Computer:
    def __init__(self, break_on_first_rcv):
        self._break_on_first_rcv = break_on_first_rcv
        self._most_recently_played_sound = None
        self._registers = defaultdict(lambda: 0)
        self._index = 0

    def recovered_frequency(self, instructions):
        try:
            self._follow_instructions(instructions)
        except FirstRcvReachedException as e:
            return e.args[0]

    def _follow_instructions(self, instructions):
        while 0 <= self._index < len(instructions):
            self._follow_instruction(instructions[self._index])

    def _follow_instruction(self, list_):
        instruction, *params = list_
        print(instruction, params)
        if instruction == 'snd':
            self._most_recently_played_sound = self._to_value(params[0])
        elif instruction == 'set':
            self._registers[params[0]] = self._to_value(params[1])
        elif instruction == 'add':
            self._registers[params[0]] += self._to_value(params[1])
        elif instruction == 'mul':
            self._registers[params[0]] *= self._to_value(params[1])
        elif instruction == 'mod':
            self._registers[params[0]] %= self._to_value(params[1])
        elif instruction == 'rcv':
            if self._break_on_first_rcv and self._to_value(params[0]) != 0:
                raise FirstRcvReachedException(self._most_recently_played_sound)
        elif instruction == 'jgz':
            if self._to_value(params[0]) > 0:
                self._index += self._to_value(params[1])
                return
        self._index += 1

    def _to_value(self, value_or_register):
        try:
            return int(value_or_register)
        except ValueError:
            return self._registers[value_or_register]


class FirstRcvReachedException(Exception):
    pass


if __name__ == '__main__':
    computer = Computer(break_on_first_rcv=True)
    print(computer.recovered_frequency(input_lists(18, delimiter=' ')))
