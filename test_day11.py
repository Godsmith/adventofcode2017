import pytest

from day11 import distance_from_string, Position


@pytest.mark.parametrize('input_, distance',
                         [('ne,ne,ne', 3),
                          ('ne,ne,sw,sw', 0),
                          ('ne,ne,s,s', 2),
                          ('se,sw,se,sw,sw', 3)])
def test_distance_from_string(input_, distance):
    assert distance_from_string(input_) == distance


class TestPosition:
    @pytest.mark.parametrize('y, x, direction, new_y, new_x',
                             [(1, 1, 'nw', 0, 0),
                              (1, 1, 'n', 0, 1),
                              (1, 1, 'ne', 0, 2),
                              (1, 1, 'se', 1, 2),
                              (1, 1, 's', 2, 1),
                              (1, 1, 'sw', 1, 0)])
    def test_walk(self, y, x, direction, new_y, new_x):
        position = Position(y, x).walk(direction)
        assert new_y == position.y
        assert new_x == position.x

    def test_equal(self):
        assert Position(5, 3) == Position(5, 3)

    def test_hash(self):
        assert hash(Position(5, 3)) == hash(Position(5, 3))
