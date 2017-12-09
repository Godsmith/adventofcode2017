import pytest

from day9 import score, score_and_garbage_count


@pytest.mark.parametrize('input_,expected',
                         [('{}', 1),
                          ('{{{}}}', 6),
                          ('{{},{}}', 5),
                          ('{{{},{},{{}}}}', 16),
                          ('{<a>,<a>,<a>,<a>}', 1),
                          ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
                          ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
                          ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)])
def test_score(input_, expected):
    assert score(input_) == expected


@pytest.mark.parametrize('input_,expected',
                         [('<>', 0),
                          ('<random characters>', 17),
                          ('<<<<>', 3),
                          ('<{!>}>', 2),
                          ('<!!>', 0),
                          ('<!!!>>', 0),
                          ('<{o"i!a,<{i<a>,', 10)])
def test_garbage_count(input_, expected):
    assert score_and_garbage_count(input_)[1] == expected
