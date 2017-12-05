from day1 import current_and_next, solve_captcha


def test_current_and_next():
    assert list(current_and_next('123')) == [("1", "2"), ("2", "3"), ("3", "1")]


def test_solve_captcha():
    assert solve_captcha('1122') == 3
    assert solve_captcha('1111') == 4
    assert solve_captcha('1234') == 0
    assert solve_captcha('91212129') == 9
