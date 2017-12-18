from collections import deque

from day16 import spin, exchange, partner, partial_function_from_string, \
    dance, TranslatorFactory, Translator
from util import input_list


def test_spin():
    assert spin(deque('abcde'), 1) == deque('eabcd')


def test_exchange():
    assert exchange(deque('eabcd'), 3, 4) == deque('eabdc')


def test_partner():
    assert partner(deque('eabdc'), 'e', 'b') == deque('baedc')


def test_partial_function_from_string():
    d = deque('abcde')
    f1 = partial_function_from_string('s1')
    f2 = partial_function_from_string('x3/4')
    f3 = partial_function_from_string('pe/b')
    assert f3(f2(f1(d))) == deque('baedc')


def test_dance():
    assert dance(deque('abcde'), ['s1', 'x3/4', 'pe/b']) == deque('baedc')
    assert (dance(deque('abcde'), ['s1', 'x3/4', 'pe/b']) ==
            dance(deque('abcde'), ['pe/b', 's1', 'x3/4']))


class TestTranslator:
    def test_from_list(self):
        translator = Translator.from_list(['pe/b', 's1', 'x3/4'], 5)
        assert ''.join(translator.translate('abcde')) == 'baedc'

    def test_add(self):
        translator = Translator.from_list(['pe/b', 's1', 'x3/4'], 5)
        translator2 = translator + translator
        assert ''.join(translator2.translate('abcde')) == 'ceadb'


class TestTranslatorFactory:
    def test_repeated_translators_puzzle_input(self):
        factory = TranslatorFactory(2)
        translator = factory.create_repeated_translators(
            ['pe/b', 's1', 'x3/4'], length=5)
        assert ''.join(translator.translate('abcde')) == 'ceadb'

    def test_part_two(self):
        factory = TranslatorFactory(1000000000)
        translator = factory.create_repeated_translators(input_list(16), 16)
        assert ''.join(
            translator.translate('abcdefghijklmnop')) == 'hklecbpnjigoafmd'
