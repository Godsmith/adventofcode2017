from day1 import solve_captcha, solve_captcha_part_two, current_and_offset


def test_current_and_offset():
    assert list(current_and_offset('123', 1)) == [("1", "2"),
                                                  ("2", "3"),
                                                  ("3", "1")]
    assert list(current_and_offset('1234', 2)) == [("1", "3"),
                                                   ("2", "4"),
                                                   ("3", "1"),
                                                   ("4", "2")]


def test_solve_captcha():
    assert solve_captcha('1122') == 3
    assert solve_captcha('1111') == 4
    assert solve_captcha('1234') == 0
    assert solve_captcha('91212129') == 9


def test_solve_captcha_part_two():
    assert solve_captcha_part_two('1212') == 6
    assert solve_captcha_part_two('1221') == 0
    assert solve_captcha_part_two('123425') == 4
    assert solve_captcha_part_two('123123') == 12
    assert solve_captcha_part_two('12131415') == 4
