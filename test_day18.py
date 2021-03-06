from day18 import SoundRecoverProgram

INSTRUCTIONS = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""".split('\n')


def test_recovered_frequency():
    computer = SoundRecoverProgram(break_on_first_rcv=True)
    assert computer.recovered_frequency(INSTRUCTIONS) == 4
