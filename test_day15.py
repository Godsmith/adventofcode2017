from day15 import generator_a, generator_b, judge, match, \
    generator_a_part_2, generator_b_part_2


def test_generator_a():
    a = generator_a(65)
    assert next(a) == 1092455
    assert next(a) == 1181022009


def test_generator_b():
    b = generator_b(8921)
    assert next(b) == 430625591
    assert next(b) == 1233683848


def test_generator_a_and_b_part_2():
    a = generator_a_part_2(65)
    b = generator_b_part_2(8921)
    assert next(a) == 1352636452
    assert next(b) == 1233683848
    assert next(a) == 1992081072
    assert next(b) == 862516352


def test_match():
    assert match(245556042, 1431495498)


def test_judge():
    assert judge(65, 8921, 5) == 1
    assert judge(65, 8921, 1055, generator_a_part_2, generator_b_part_2) == 0
    assert judge(65, 8921, 1056, generator_a_part_2, generator_b_part_2) == 1
