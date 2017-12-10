import pytest

from day10 import tie_knot, knot_hash, reverse_part, \
    parse_input_for_part_two, dense_hash, my_hex, dense_hash_string, \
    knot_hash_string


def test_reverse_part():
    assert reverse_part([2, 1, 0, 3, 4], start=3, length=4) == [4, 3, 0, 1, 2]


@pytest.mark.parametrize('list_, current_position, input_, skip, '
                         'new_list, new_position, new_skip',
                         [([0, 1, 2, 3, 4], 0, 3, 0,
                           [2, 1, 0, 3, 4], 3, 1),
                          ([2, 1, 0, 3, 4], 3, 4, 1,
                           [4, 3, 0, 1, 2], 3, 2)])
def test_tie_knot(list_, current_position, input_, skip, new_list,
                  new_position, new_skip):
    assert tie_knot(
        list_=list_,
        current_position=current_position,
        input_=input_,
        skip=skip) == (new_list, new_position, new_skip)


@pytest.mark.parametrize('list_, inputs, output',
                         [([0, 1, 2, 3, 4], [3], [2, 1, 0, 3, 4]),
                          ([0, 1, 2, 3, 4], [3, 4], [4, 3, 0, 1, 2]),
                          ([0, 1, 2, 3, 4], [3, 4, 1, 5], [3, 4, 2, 1, 0])])
def test_tie_knots(list_, inputs, output):
    knot_hash_list, _, _ = knot_hash(list_, inputs)
    assert knot_hash_list == output


def test_parse_input_for_part_two():
    assert parse_input_for_part_two('1,2,3') == [49, 44, 50, 44, 51, 17, 31, 73,
                                                 47, 23]


def test_dense_hash():
    hash = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    assert dense_hash(hash) == [64]
    assert len(dense_hash(range(256))) == 16


def test_dense_hash_string():
    assert dense_hash_string([64, 7, 255]) == '4007ff'


def test_my_hex():
    assert my_hex(64) == '40'


def test_knot_hash_string():
    assert knot_hash_string('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot_hash_string('') == 'a2582a3a0e66e6e86e3812dcb672a272'
