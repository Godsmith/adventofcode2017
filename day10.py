from functools import reduce
from operator import xor

INPUT_STRING = '63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24'
INPUT_PART_1 = map(int, INPUT_STRING.split(','))


def parse_input_for_part_two(input_string):
    return list(map(ord, input_string)) + [17, 31, 73, 47, 23]


class HalfTwist:
    @classmethod
    def tie_knot(cls, list_, position, length, skip):
        new_list = cls._reverse_part(list_, position, length)
        return new_list, (position + length + skip) % len(
            list_), skip + 1

    @classmethod
    def _reverse_part(cls, list_, start, length):
        old_indices = [i % len(list_) for i in range(start, start + length)]
        new_indices = reversed(old_indices)
        new_list = list(list_)
        for old, new in zip(old_indices, new_indices):
            new_list[new] = list_[old]
        return new_list


class HashCondenser:
    def __init__(self, sparse_hash):
        self._sparse_hash = sparse_hash

    def __call__(self):
        return self.dense_hash_string(self.dense_hash(self._sparse_hash))

    @classmethod
    def dense_hash(cls, sparse_hash_):
        return [reduce(xor, sparse_hash_[i:i + 16])
                for i in range(0, len(sparse_hash_), 16)]

    @classmethod
    def dense_hash_string(cls, dense_hash_list):
        return ''.join(map(cls.my_hex, dense_hash_list))

    @classmethod
    def my_hex(cls, int_):
        s = hex(int_)[2:]
        if len(s) == 1:
            return '0' + s
        return s


class KnotHash:
    def __init__(self, inputs=None):
        self.inputs = inputs

    def knot_hash(self, list_, position=0, skip=0):
        for input_ in self.inputs:
            list_, position, skip = HalfTwist.tie_knot(list_, position, input_,
                                                       skip)
        return list_, position, skip

    def sparse_hash(self, list_):
        position = 0
        skip = 0
        for _ in range(64):
            list_, position, skip = self.knot_hash(list_, position, skip)
        return list_

    def knot_hash_string(self):
        self.inputs = parse_input_for_part_two(self.inputs)
        sparse_hash_ = self.sparse_hash(list(range(256)))
        return HashCondenser(sparse_hash_)()


if __name__ == '__main__':
    list_ = list(range(256))
    knot_hash = KnotHash(INPUT_PART_1)
    output_list, _, _ = knot_hash.knot_hash(list_)
    print(output_list[0] * output_list[1])

    print(knot_hash.knot_hash_string())
