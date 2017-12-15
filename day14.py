from day10 import KnotHash


def row_strings(input_):
    return [f'{input_}-{i}' for i in range(128)]


def binary_from_hex(hex_):
    return bin(int(hex_, 16)).split('b')[-1].zfill(4)


def binary_knot_hash(input_):
    hexadecimal = [str(KnotHash(row_input))
                   for row_input in row_strings(input_)]
    binary = [''.join(map(binary_from_hex, row))
              for row in hexadecimal]
    return binary


def used_squares(input_):
    hash_rows = binary_knot_hash(input_)
    return sum(row.count('1') for row in hash_rows)


if __name__ == '__main__':
    print(used_squares('jzgqcdpd'))
