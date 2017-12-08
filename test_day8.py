import pytest

from day8 import largest_value, translate, register_names

INSTRUCTIONS = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".split('\n')


def test_largest_value():
    assert 1, 10 == largest_value(INSTRUCTIONS)


@pytest.mark.parametrize('input,expected',
                         [('b inc 5 if a > 1', 'if a > 1: b += 5'),
                          ('a inc 1 if b < 5', 'if b < 5: a += 1'),
                          ('c dec -10 if a >= 1', 'if a >= 1: c -= -10'),
                          ('c inc -20 if c == 10', 'if c == 10: c += -20')])
def test_translate(input, expected):
    assert translate(input) == expected


def test_register_names():
    assert register_names(INSTRUCTIONS) == {'a', 'b', 'c'}
