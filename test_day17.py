from blist import blist

from day17 import spinlock


def test_spinlock():
    lock = spinlock(3)
    assert next(lock) == blist([0, 1])
    assert next(lock) == blist([0, 2, 1])
    assert next(lock) == blist([0, 2, 3, 1])
    assert next(lock) == blist([0, 2, 4, 3, 1])
