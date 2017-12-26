from day21 import Square


class TestSquare:
    def test_break_up_size_4(self):
        square = Square.from_string('####/####/..../....')
        assert square.break_up() == [Square.from_string('##/##'),
                                     Square.from_string('##/##'),
                                     Square.from_string('../..'),
                                     Square.from_string('../..')]

    def test_break_up_size_3(self):
        square = Square.from_string('###/###/...')
        assert square.break_up() == [Square.from_string('###/###/...')]

    def test_combine(self):
        assert Square.from_string('.###/####/#.../....') == \
               Square.combine([Square.from_string('.#/##'),
                               Square.from_string('##/##'),
                               Square.from_string('#./..'),
                               Square.from_string('../..')])
