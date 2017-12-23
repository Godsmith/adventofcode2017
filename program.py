from collections import defaultdict


class BaseProgram:
    def __init__(self):
        self._registers = defaultdict(lambda: 0)
        self._index = 0

    def _follow_instruction(self, list_):
        instruction, *params = list_
        print(instruction, params)
        if instruction == 'snd':
            self._snd(params)
        elif instruction == 'set':
            self._registers[params[0]] = self._to_value(params[1])
        elif instruction == 'add':
            self._registers[params[0]] += self._to_value(params[1])
        elif instruction == 'mul':
            self._registers[params[0]] *= self._to_value(params[1])
        elif instruction == 'mod':
            self._registers[params[0]] %= self._to_value(params[1])
        elif instruction == 'rcv':
            self._rcv(params)
        elif instruction == 'jgz':
            if self._to_value(params[0]) > 0:
                self._index += self._to_value(params[1])
                return
        self._index += 1

    def _snd(self, params):
        raise NotImplementedError

    def _rcv(self, params):
        raise NotImplementedError

    def _follow_instructions(self, instructions):
        while 0 <= self._index < len(instructions):
            self._follow_instruction(instructions[self._index])

    def _to_value(self, value_or_register):
        try:
            return int(value_or_register)
        except ValueError:
            return self._registers[value_or_register]


class FirstRcvReachedException(Exception):
    pass
