from day15 import generator_a, generator_b, last_16_bits, judge, match


def test_generator_a():
    a = generator_a(65)
    assert next(a) == 1092455
    assert next(a) == 1181022009


def test_generator_b():
    b = generator_b(8921)
    assert next(b) == 430625591
    assert next(b) == 1233683848


def test_last_16_bits():
    assert last_16_bits(1092455) == '1010101101100111'
    assert last_16_bits(1) == '0000000000000001'


def test_match():
    assert match(245556042, 1431495498)


def test_judge():
    assert judge(65, 8921, 5) == 1
