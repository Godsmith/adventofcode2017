from day6 import cycle, cycle_count_and_loop_size


def test_cycle():
    assert cycle((0, 2, 7, 0)) == (2, 4, 1, 2)
    assert cycle((2, 4, 1, 2)) == (3, 1, 2, 3)
    assert cycle((3, 1, 2, 3)) == (0, 2, 3, 4)
    assert cycle((0, 2, 3, 4)) == (1, 3, 4, 1)
    assert cycle((1, 3, 4, 1)) == (2, 4, 1, 2)


def test_count_cycles():
    banks = (0, 2, 7, 0)
    assert cycle_count_and_loop_size(banks) == (5, 4)
