from blist import blist


def spinlock(steps):
    list_ = blist([0])
    position = 0
    length = 1
    while True:
        position = (position + steps) % length
        list_.insert(position + 1, length)
        position = position + 1
        length += 1
        yield list_


def spinlock_value_after_value(steps, iterations, value):
    lock = spinlock(steps)
    for _ in range(iterations):
        list_ = next(lock)
    return list_[list_.index(value) + 1]


def spinlock_value_after_0(steps, iterations):
    """More optimized version of this special case"""
    position_of_0 = 0
    position = 0
    length = 1
    value_after_0 = None
    for _ in range(iterations):
        position = (position + steps) % length
        if position < position_of_0:
            position_of_0 += 1
        elif position == position_of_0:
            value_after_0 = length
        position += 1
        length += 1
    return value_after_0


if __name__ == '__main__':
    print(spinlock_value_after_value(303, 2017, 2017))
    print(spinlock_value_after_0(303, 50000000))
