A_START = 591
B_START = 393


def generator_a(value):
    FACTOR = 16807
    while True:
        value = (value * FACTOR) % 2147483647
        yield value


def generator_a_part_2(value):
    FACTOR = 16807
    while True:
        value = (value * FACTOR) % 2147483647
        if value % 4 == 0:
            yield value


def generator_b(value):
    FACTOR = 48271
    while True:
        value = (value * FACTOR) % 2147483647
        yield value


def generator_b_part_2(value):
    FACTOR = 48271
    while True:
        value = (value * FACTOR) % 2147483647
        if value % 8 == 0:
            yield value


def judge(value_a, value_b, iterations, gen_a=generator_a, gen_b=generator_b):
    a = gen_a(value_a)
    b = gen_b(value_b)
    return sum(match(next(a), next(b)) for _ in range(iterations))


MASK = (1 << 16) - 1


def match(a, b):
    return a & MASK == b & MASK


if __name__ == '__main__':
    print(judge(A_START, B_START, 40000000))
    print(judge(A_START, B_START, 5000000,
                generator_a_part_2, generator_b_part_2))
