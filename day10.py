from functools import reduce
from operator import xor

INPUT_STRING = '63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24'
INPUT_PART_1 = map(int, INPUT_STRING.split(','))


def parse_input_for_part_two(input_string):
    return list(map(ord, input_string)) + [17, 31, 73, 47, 23]


def tie_knot(list_, current_position, input_, skip):
    new_list = reverse_part(list_, current_position, input_)
    return new_list, (current_position + input_ + skip) % len(list_), skip + 1


def reverse_part(list_, start, length):
    old_indices = [i % len(list_) for i in range(start, start + length)]
    new_indices = reversed(old_indices)
    new_list = list(list_)
    for old, new in zip(old_indices, new_indices):
        new_list[new] = list_[old]
    return new_list


def knot_hash(list_, inputs, position=0, skip=0):
    for input_ in inputs:
        list_, position, skip = tie_knot(list_, position, input_, skip)
    return list_, position, skip


def sparse_hash(list_, inputs):
    position = 0
    skip = 0
    for _ in range(64):
        list_, position, skip = knot_hash(list_, inputs, position, skip)
    return list_


def dense_hash(sparse_hash_):
    return [reduce(xor, sparse_hash_[i:i + 16])
            for i in range(0, len(sparse_hash_), 16)]


def dense_hash_string(dense_hash_list):
    return ''.join(map(my_hex, dense_hash_list))


def my_hex(int_):
    s = hex(int_)[2:]
    if len(s) == 1:
        return '0' + s
    return s


def knot_hash_string(input_):
    input_list = parse_input_for_part_two(input_)
    sparse_hash_ = sparse_hash(list(range(256)), input_list)
    dense_hash_ = dense_hash(sparse_hash_)
    return dense_hash_string(dense_hash_)


if __name__ == '__main__':
    list_ = list(range(256))
    output_list, _, _ = knot_hash(list_, INPUT_PART_1)
    print(output_list[0] * output_list[1])

    print(knot_hash_string(INPUT_STRING))
