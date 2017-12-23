from collections import defaultdict


class BaseProgram:
    def __init__(self):
        self._registers = defaultdict(lambda: 0)
        self._index = 0

    def follow_instruction(self, instructions):
        instruction, *params = instructions[self._index].split()
        method = getattr(self, f'_{instruction}')
        method(params)
        self._index += 1

    def _jgz(self, params):
        if self._to_value(params[0]) > 0:
            self._index += self._to_value(params[1]) - 1
            return

    def _mod(self, params):
        self._registers[params[0]] %= self._to_value(params[1])

    def _mul(self, params):
        self._registers[params[0]] *= self._to_value(params[1])

    def _add(self, params):
        self._registers[params[0]] += self._to_value(params[1])

    def _set(self, params):
        self._registers[params[0]] = self._to_value(params[1])

    def _snd(self, params):
        raise NotImplementedError

    def _rcv(self, params):
        raise NotImplementedError

    def _to_value(self, value_or_register):
        try:
            return int(value_or_register)
        except ValueError:
            return self._registers[value_or_register]

    def follow_instructions(self, instructions):
        while 0 <= self._index < len(instructions):
            self.follow_instruction(instructions)


class FirstRcvReachedException(Exception):
    pass
