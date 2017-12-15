A_START = 591
B_START = 393


def generator_a(value):
    FACTOR = 16807
    while True:
        value = (value * FACTOR) % 2147483647
        yield value


def generator_b(value):
    FACTOR = 48271
    while True:
        value = (value * FACTOR) % 2147483647
        yield value


def judge(value_a, value_b, iterations):
    a = generator_a(value_a)
    b = generator_b(value_b)
    sum_ = 0
    for i in range(iterations):
        sum_ += match(next(a), next(b))
        print(i)
    return sum_

    # return sum(match(next(a), next(b)) for _ in range(iterations))


MASK = (1 << 16) - 1


def match(a, b):
    return last_16_bits(a) == last_16_bits(b)


def last_16_bits(int_):
    return '{:016b}'.format(int_)[-16:]


if __name__ == '__main__':
    print(judge(A_START, B_START, 40000000))
