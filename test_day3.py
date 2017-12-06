from day3 import distance_to_center, AdjacencySpiralSquare


def test_distance_to_center():
    assert distance_to_center(5, 1) == 0
    assert distance_to_center(5, 12) == 3
    assert distance_to_center(5, 23) == 2
    assert distance_to_center(33, 1024) == 31

def test_adjancency_spiral_square():
    assert AdjacencySpiralSquare(5).table[0] == [147, 142, 133, 122, 59]
