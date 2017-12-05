"""Collection of methods used by several problems
"""
import os


def input_rows(day_nr):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open('%s\\inputs\\day%s.txt' % (current_dir, day_nr)) as f:
        return list(line.strip() for line in f.readlines())


def test_input_rows():
    assert input_rows('test') == ['hello', 'world']
