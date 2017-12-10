import pytest

from day10 import KnotHash, parse_input_for_part_two, HalfTwist, HashCondenser


class TestHalfTwist:
    def test_reverse_part(self):
        assert HalfTwist._reverse_part([2, 1, 0, 3, 4], start=3, length=4) == \
               [4, 3, 0, 1, 2]

    @pytest.mark.parametrize('list_, current_position, input_, skip, '
                             'new_list, new_position, new_skip',
                             [([0, 1, 2, 3, 4], 0, 3, 0,
                               [2, 1, 0, 3, 4], 3, 1),
                              ([2, 1, 0, 3, 4], 3, 4, 1,
                               [4, 3, 0, 1, 2], 3, 2)])
    def test_tie_knot(self, list_, current_position, input_, skip, new_list,
                      new_position, new_skip):
        assert HalfTwist.tie_knot(
            list_=list_,
            position=current_position,
            length=input_,
            skip=skip) == (new_list, new_position, new_skip)


class TestHashCondenser:
    def test_dense_hash(self):
        hash_ = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
        assert HashCondenser(hash_)._dense_hash() == [64]
        assert len(HashCondenser(range(256))._dense_hash()) == 16

    def test_dense_hash_string(self):
        assert HashCondenser._dense_hash_string([64, 7, 255]) == '4007ff'

    def test_my_hex(self):
        assert HashCondenser._my_hex(64) == '40'


class TestKnotHash:
    def test_str(self):
        assert str(KnotHash('AoC 2017')) == \
               '33efeb34ea91902bb2f59c9920caa6cd'
        assert str(KnotHash('')) == 'a2582a3a0e66e6e86e3812dcb672a272'

    @pytest.mark.parametrize('list_, inputs, output',
                             [([0, 1, 2, 3, 4], [3], [2, 1, 0, 3, 4]),
                              ([0, 1, 2, 3, 4], [3, 4], [4, 3, 0, 1, 2]),
                              ([0, 1, 2, 3, 4], [3, 4, 1, 5], [3, 4, 2, 1, 0])])
    def test_knot_hash(self, list_, inputs, output):
        knot_hash_list, _, _ = KnotHash(inputs)._single_round(list_)
        assert knot_hash_list == output


def test_parse_input_for_part_two():
    assert parse_input_for_part_two('1,2,3') == [49, 44, 50, 44, 51,
                                                 17, 31, 73,
                                                 47, 23]
