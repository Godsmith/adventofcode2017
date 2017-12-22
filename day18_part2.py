from collections import defaultdict, deque

from util import input_rows


class Program:
    def __init__(self, id):
        self._id = id
        self._registers = defaultdict(lambda: 0)
        self._registers['p'] = id
        self._index = 0
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
            self.send_count += 1
            self._peer_program.send(self._to_value(params[0]))
        elif instruction == 'set':
            self._registers[params[0]] = self._to_value(params[1])
        elif instruction == 'add':
            self._registers[params[0]] += self._to_value(params[1])
        elif instruction == 'mul':
            self._registers[params[0]] *= self._to_value(params[1])
        elif instruction == 'mod':
            self._registers[params[0]] %= self._to_value(params[1])
        elif instruction == 'rcv':
            if len(self._message_queue) == 0:
                self.waiting = True
                return
            self._registers[params[0]] = self._message_queue.pop()
            self.waiting = False
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


def send_count_of_second_program_at_deadlock(programs, instructions):
    programs[0].peer(programs[1])
    while any([not p.waiting for p in programs]):
        for p in programs:
            p.follow_instruction(instructions)
    return programs[1].send_count


if __name__ == '__main__':
    p0 = Program(0)
    p1 = Program(1)
    print(send_count_of_second_program_at_deadlock([p0, p1], input_rows(18)))
