from day15 import Judge, GeneratorFactory


def test_generator_a():
    a = GeneratorFactory.create('a', 1, 65)
    assert next(a) == 1092455
    assert next(a) == 1181022009


def test_generator_b():
    b = GeneratorFactory.create('b', 1, 8921)
    assert next(b) == 430625591
    assert next(b) == 1233683848


def test_generator_a_and_b_part_2():
    a = GeneratorFactory.create('a', 2, 65)
    b = GeneratorFactory.create('b', 2, 8921)
    assert next(a) == 1352636452
    assert next(b) == 1233683848
    assert next(a) == 1992081072
    assert next(b) == 862516352


def test_match():
    assert Judge._match(245556042, 1431495498)


def test_judge():
    generator_a_part_1 = GeneratorFactory.create('a', 1, 65)
    generator_b_part_1 = GeneratorFactory.create('b', 1, 8921)
    generator_a_part_2 = GeneratorFactory.create('a', 2, 65)
    generator_b_part_2 = GeneratorFactory.create('b', 2, 8921)
    assert Judge(generator_a_part_1, generator_b_part_1).judge(5) == 1
    assert Judge(generator_a_part_2, generator_b_part_2).judge(1055) == 0
    assert Judge(generator_a_part_2, generator_b_part_2).judge(1056) == 1
