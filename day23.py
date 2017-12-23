from program import BaseProgram
from util import input_rows


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
    program = ExperimentalProgram()
    program.follow_instructions(input_)
    print(program.mul_count)
