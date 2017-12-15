from day10 import KnotHash
from day14 import row_strings, binary_from_hex, binary_knot_hash, \
    used_squares, count_regions

INPUT = 'flqrgnkx'


def test_row_strings():
    assert row_strings(INPUT)[127] == 'flqrgnkx-127'


def test_binary_from_hex():
    assert binary_from_hex('0') == '0000'
    assert binary_from_hex('1') == '0001'
    assert binary_from_hex('e') == '1110'
    assert binary_from_hex('f') == '1111'


def test_knot_hash():
    first_row_hexadecimal = str(KnotHash(row_strings(INPUT)[0]))
    first_row_binary = ''.join(map(binary_from_hex, first_row_hexadecimal))
    assert first_row_binary.startswith('11010100')


def test_binary_knot_hash():
    assert binary_knot_hash(INPUT)[0].startswith('11010100')


def test_used_squares():
    assert used_squares(INPUT) == 8108


def test_count_regions():
    table = \
        """110101
010101
000010
101011
011010
110010"""
    assert count_regions(table.split('\n')) == 6
