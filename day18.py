from program import BaseProgram, FirstRcvReachedException
from util import input_rows


class SoundRecoverProgram(BaseProgram):
    def __init__(self, break_on_first_rcv):
        super().__init__()
        self._break_on_first_rcv = break_on_first_rcv
        self._most_recently_played_sound = None

    def recovered_frequency(self, instructions):
        try:
            self._follow_instructions(instructions)
        except FirstRcvReachedException as e:
            return e.args[0]

    def _follow_instructions(self, instructions):
        while 0 <= self._index < len(instructions):
            self.follow_instruction(instructions)

    def _rcv(self, params):
        if self._break_on_first_rcv and self._to_value(params[0]) != 0:
            raise FirstRcvReachedException(self._most_recently_played_sound)

    def _snd(self, params):
        self._most_recently_played_sound = self._to_value(params[0])


if __name__ == '__main__':
    computer = SoundRecoverProgram(break_on_first_rcv=True)
    print(computer.recovered_frequency(input_rows(18)))
