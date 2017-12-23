from program import BaseProgram
from util import input_rows

INSTRUCTIONS = """set b 65
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set e b
set g 0
sub d -1
set g d
sub g b
jnz g -6
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -10
jnz 1 -16
d""".split('\n')


class ExperimentalProgram(BaseProgram):
    def __init__(self):
        super().__init__()
        self.mul_count = 0

    def _mul(self, params):
        self.mul_count += 1
        super()._mul(params)

    def _jnz(self, params):
        if self._to_value(params[0]) != 0:
            self._index += self._to_value(params[1]) - 1

    def _sub(self, params):
        self._registers[params[0]] -= self._to_value(params[1])


if __name__ == '__main__':
    input_ = input_rows(23)
    # program = ExperimentalProgram()
    # program.follow_instructions(input_)
    # print(program.mul_count)

    program = ExperimentalProgram()
    program._registers['a'] = 1
    program.follow_instructions(INSTRUCTIONS)
    print(program._registers['h'])
