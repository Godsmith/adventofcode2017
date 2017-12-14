from day12 import Program, programs_from_strings, group_including_program, \
    groups

INPUT = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".split('\n')


def test_programs():
    d = programs_from_strings(INPUT)
    assert len(d) == 7
    assert d[4].connections == [2, 3, 6]


def test_group_including_program():
    assert 6 == len(group_including_program(INPUT, 0))
    assert 1 == len(group_including_program(INPUT, 1))


def test_groups():
    assert 2 == len(groups(INPUT))


class TestProgram:
    def test_from_string(self):
        p = Program.from_string('0 <-> 2')
        assert p.id == 0
        assert p.connections == [2]
