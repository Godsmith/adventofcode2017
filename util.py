"""Collection of methods used by several problems
"""
import os


def input_rows(day_nr):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open('%s\\inputs\\day%s.txt' % (current_dir, day_nr)) as f:
        return list(line.strip() for line in f.readlines())


def input_lists(day_nr, delimiter='\t'):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open('%s\\inputs\\day%s.txt' % (current_dir, day_nr)) as f:
        return list(line.strip().split(delimiter) for line in f.readlines())


def input_list(day_nr, delimiter=','):
    return input_lists(day_nr, delimiter)[0]


def test_input_rows():
    assert input_rows('test') == ['hello', 'world']


def test_input_lists():
    assert input_lists('test_lists') == [['hello', 'world', 'again'],
                                         ['how', 'are', 'you']]


def test_input_list():
    assert input_list('test_list') == ['1', '2', '3', '4', '5']
