from collections import deque

from program import BaseProgram
from util import input_rows


class DuetProgram(BaseProgram):
    def __init__(self, id):
        super().__init__()
        self._registers['p'] = id
        self._message_queue = deque()
        self._peer_program = None
        self.send_count = 0
        self.waiting = False
        self.terminated = True

    def peer(self, program):
        self._peer_program = program
        program._peer_program = self

    def send(self, value):
        self._message_queue.appendleft(value)

    def follow_instruction(self, instructions):
        if not 0 <= self._index < len(instructions):
            self.waiting = True
            return
        instruction, *params = instructions[self._index].split()
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
        self.send_count += 1
        self._peer_program.send(self._to_value(params[0]))

    def _rcv(self, params):
        if len(self._message_queue) == 0:
            self.waiting = True
            self._index -= 1  # stay in place
            return
        self._registers[params[0]] = self._message_queue.pop()
        self.waiting = False

    def _to_value(self, value_or_register):
        try:
            return int(value_or_register)
        except ValueError:
            return self._registers[value_or_register]


def send_count_of_second_program_at_deadlock(programs, instructions):
    programs[0].peer(programs[1])
    while any([not p.waiting for p in programs]):
        for p in programs:
            p.follow_instruction(instructions)
    return programs[1].send_count


if __name__ == '__main__':
    p0 = DuetProgram(0)
    p1 = DuetProgram(1)
    print(send_count_of_second_program_at_deadlock([p0, p1], input_rows(18)))
