from blist import blist

from day17 import spinlock, spinlock_value_after_value, spinlock_value_after_0


def test_spinlock():
    lock = spinlock(3)
    assert next(lock) == blist([0, 1])
    assert next(lock) == blist([0, 2, 1])
    assert next(lock) == blist([0, 2, 3, 1])
    assert next(lock) == blist([0, 2, 4, 3, 1])


def test_spinlock_value_after_value():
    assert spinlock_value_after_value(303, 2017, 2017) == 1971


def test_spinlock_value_after_0():
    assert (spinlock_value_after_0(303, 2017) ==
            spinlock_value_after_value(303, 2017, 0))
