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
    return list_[list_.index(2017) + 1]


if __name__ == '__main__':
    print(spinlock_value_after_value(303, 2017, 2017))
    print(spinlock_value_after_value(303, 50000000, 0))
