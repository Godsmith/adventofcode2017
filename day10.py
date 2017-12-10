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
        self.sparse_hash = sparse_hash

    def condense(self):
        return self._dense_hash_string(self._dense_hash())

    def _dense_hash(self):
        return [reduce(xor, self.sparse_hash[i:i + 16])
                for i in range(0, len(self.sparse_hash), 16)]

    @classmethod
    def _dense_hash_string(cls, dense_hash_list):
        return ''.join(map(cls._my_hex, dense_hash_list))

    @classmethod
    def _my_hex(cls, int_):
        s = hex(int_)[2:]
        if len(s) == 1:
            return '0' + s
        return s


class KnotHash:
    def __init__(self, inputs=None):
        self.inputs = inputs

    def _single_round(self, list_, position=0, skip=0):
        for input_ in self.inputs:
            list_, position, skip = HalfTwist.tie_knot(list_, position, input_,
                                                       skip)
        return list_, position, skip

    def _sparse_hash(self, list_):
        position = 0
        skip = 0
        for _ in range(64):
            list_, position, skip = self._single_round(list_, position, skip)
        return list_

    def __str__(self):
        self.inputs = parse_input_for_part_two(self.inputs)
        sparse_hash = self._sparse_hash(list(range(256)))
        return HashCondenser(sparse_hash).condense()


if __name__ == '__main__':
    list_ = list(range(256))
    knot_hash = KnotHash(INPUT_PART_1)
    output_list, _, _ = knot_hash._single_round(list_)
    print(output_list[0] * output_list[1])

    print(KnotHash(INPUT_STRING))
