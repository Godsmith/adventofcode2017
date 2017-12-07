import pytest

from day7 import bottom_program, ProgramParser, faulty_program, \
    correct_weight_of_faulty_program

INPUT = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


@pytest.fixture
def programs():
    input_rows = INPUT.split('\n')
    return ProgramParser.create_programs(input_rows)


def test_bottom_program(programs):
    assert bottom_program(programs).name == 'tknk'


def test_faulty_program(programs):
    assert faulty_program(programs).name == 'ugml'


def test_correct_weight_of_faulty_program(programs):
    assert correct_weight_of_faulty_program(programs) == 60
