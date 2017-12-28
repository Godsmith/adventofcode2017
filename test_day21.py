from day21 import Square, EnhancementBook

from util import input_rows


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

    def test_rotate(self):
        square = Square.from_string('###/###/...')
        assert square._rotate() == Square.from_string('.##/.##/.##')
        assert square._rotate()._rotate() == Square.from_string('.../###/###')

    def test_rotations(self):
        square = Square.from_string('###/###/...')
        assert square._rotations() == {square,
                                       Square.from_string('.##/.##/.##'),
                                       Square.from_string('.../###/###'),
                                       Square.from_string('##./##./##.')}

    def test_rotations_harder(self):
        square = Square.from_string('.#./..#/###')
        assert square._rotations() == {square,
                                       Square.from_string('.#./#../###'),
                                       Square.from_string('.../###/###'),
                                       Square.from_string('##./##./##.')}

    def test_enhance(self):
        square = Square.from_string('##/..')
        book = {Square.from_string('##/..'): Square.from_string('###/.../###')}
        assert square._enhance(book) == Square.from_string('###/.../###')

    def test_enhance_rotated(self):
        square = Square.from_string('##/..')
        book = {Square.from_string('#./#.'): Square.from_string('###/.../###')}
        assert square._enhance(book) == Square.from_string('###/.../###')

    def test_count_pixels_on(self):
        square = Square.from_string('##/#.')
        assert square._count_pixels_on() == 3


class TestEnhancementBook:
    def test_translate(self):
        book = EnhancementBook.from_strings(['../.. => ###/.##/#..',
                                             '#./.. => #.#/..#/#..'])
        assert book[
                   Square.from_string('#./..')] == Square.from_string(
            '#.#/..#/#..')

    def test_translate_rotated(self):
        book = EnhancementBook.from_strings(['../.. => ###/.##/#..',
                                             '#./.. => #.#/..#/#..'])
        assert book[
                   Square.from_string('../.#')] == Square.from_string(
            '#.#/..#/#..')

    def test_missing_square(self):
        book = EnhancementBook.from_strings(input_rows(21))
        assert Square.from_string('###/###/###') in book
