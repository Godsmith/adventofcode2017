from day18_part2 import Program, send_count_of_second_program_at_deadlock


class TestProgram:
    def test_init(self):
        p = Program(1)
        assert p._registers['p'] == 1


class TestSendCountOfSecondProgramAtDeadlock:
    def test_example(self):
        instructions = ['snd 1', 'snd 2', 'snd p', 'rcv a',
                        'rcv b', 'rcv c', 'rcv d']
        p0 = Program(0)
        p1 = Program(1)
        assert send_count_of_second_program_at_deadlock([p0, p1],
                                                        instructions) == 3

    def test_snd_then_rcv(self):
        instructions = ['snd 1', 'rcv a', 'snd 1'
                                          'rcv b', 'rcv c', 'rcv d']
        p0 = Program(0)
        p1 = Program(1)
        assert send_count_of_second_program_at_deadlock([p0, p1],
                                                        instructions) == 2
