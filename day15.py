class GeneratorFactory:
    @staticmethod
    def create(type, part, value):
        def _generator_part_1(value, factor):
            while True:
                value = (value * factor) % 2147483647
                yield value

        def _generator_part_2(value, factor, divisor):
            while True:
                value = (value * factor) % 2147483647
                if value % divisor == 0:
                    yield value

        if type == 'a':
            factor = 16807
            divisor = 4
        elif type == 'b':
            factor = 48271
            divisor = 8
        else:
            raise ValueError('"type" must be "a" or "b"!')
        if part == 1:
            return _generator_part_1(value, factor)
        elif part == 2:
            return _generator_part_2(value, factor, divisor)
        else:
            raise ValueError('"part" must be 1 or 2!')


class Judge:
    MASK = (1 << 16) - 1

    def __init__(self, gen_a, gen_b):
        self.gen_a = gen_a
        self.gen_b = gen_b

    def judge(self, iterations):
        return sum(self._match(next(self.gen_a), next(self.gen_b))
                   for _ in range(iterations))

    @classmethod
    def _match(cls, a, b):
        return a & cls.MASK == b & cls.MASK


if __name__ == '__main__':
    A_START = 591
    B_START = 393
    print(Judge(GeneratorFactory.create('a', 1, A_START),
                GeneratorFactory.create('b', 1, B_START)).judge(40000000))
    print(Judge(GeneratorFactory.create('a', 2, A_START),
                GeneratorFactory.create('b', 2, B_START)).judge(5000000))
