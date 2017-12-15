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


def count_regions(table):
    in_group = set()
    groups = 0
    for row_nr, row in enumerate(table):
        for col_nr, square in enumerate(row):
            if square == '1':
                if (row_nr, col_nr) not in in_group:
                    groups += 1
                    add_square_and_neighbours(table, in_group, row_nr, col_nr)
    return groups


def add_square_and_neighbours(table, set_, row_nr, col_nr):
    if (0 <= row_nr < len(table) and
                    0 <= col_nr < len(table[0]) and
                (row_nr, col_nr) not in set_ and
            table[row_nr][col_nr]) == '1':
        set_.add((row_nr, col_nr))
        add_square_and_neighbours(table, set_, row_nr + 1, col_nr)
        add_square_and_neighbours(table, set_, row_nr - 1, col_nr)
        add_square_and_neighbours(table, set_, row_nr, col_nr + 1)
        add_square_and_neighbours(table, set_, row_nr, col_nr - 1)


if __name__ == '__main__':
    print(used_squares('jzgqcdpd'))
    print(count_regions(binary_knot_hash('jzgqcdpd')))
