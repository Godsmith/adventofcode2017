from collections import deque
from string import ascii_lowercase

from util import input_list


def partial_function_from_string(s):
    if s[0] == 's':
        return spin_function(int(s[1:]))
    elif s[0] == 'x':
        index_strings = s[1:].split('/')
        index_a, index_b = map(int, index_strings)
        return exchange_function(index_a, index_b)
    else:
        a, b = s[1:].split('/')
        return partner_function(a, b)


def spin_function(x):
    def f(deque_):
        return spin(deque_, x)

    return f


def exchange_function(index_a, index_b):
    def f(deque_):
        return exchange(deque_, index_a, index_b)

    return f


def partner_function(a, b):
    def f(deque_):
        return partner(deque_, a, b)

    return f


def spin(deque_: deque, x):
    deque_.rotate(x)
    return deque_


def exchange(deque_: deque, index_a, index_b):
    a = deque_[index_a]
    deque_[index_a] = deque_[index_b]
    deque_[index_b] = a
    return deque_


def partner(deque_: deque, a, b):
    exchange(deque_, deque_.index(a), deque_.index(b))
    return deque_


def dance(deque_, strings):
    for s in strings:
        f = partial_function_from_string(s)
        f(deque_)
    return deque_


class TranslatorFactory:
    def __init__(self, iterations):
        self.translator_from_iterations = None
        self.iterations = iterations

    def create_repeated_translators(self, list_, length):
        self.translator_from_iterations = {1: Translator.from_list(list_,
                                                                   length)}
        while self._maximum_translator_iterations() < self.iterations:
            self._create_as_large_a_translator_as_possible()
        return self._largest_translator()

    def _create_as_large_a_translator_as_possible(self):
        translator, size = self._largest_translator_that_fits(self.iterations)
        combined_translator = translator + self._largest_translator()
        self.translator_from_iterations[
            self._maximum_translator_iterations() + size] = combined_translator

    def _largest_translator_that_fits(self, iterations):
        for size in reversed(sorted(self.translator_from_iterations.keys())):
            if self._maximum_translator_iterations() + size <= iterations:
                return self.translator_from_iterations[size], size

    def _largest_translator(self):
        return self.translator_from_iterations[
            self._maximum_translator_iterations()]

    def _maximum_translator_iterations(self):
        return max(self.translator_from_iterations)


class Translator:
    def __init__(self, indices_after, program_swaps_after):
        """Creates a translator with certain properties.

        :arg indices_after: The indices after swapping, e.g. 43210.
        :arg program_swaps_after: Dict with program translations,
        e.g. {'a': 'e', 'b': 'd', ...}.
        """
        self.index_translations = indices_after
        self.programs = {source: target for source, target in
                         zip(ascii_lowercase, program_swaps_after)}

    def __add__(self, other):
        new_index_translations = self._index_translate(other.index_translations)
        new_programs = self._program_swap(other.programs.values())
        return Translator(new_index_translations, new_programs)

    def translate(self, list_):
        return self._index_translate(self._program_swap(list_))

    def _program_swap(self, list_):
        return [self.programs[program] for program in list_]

    def _index_translate(self, list_):
        return [list_[self.index_translations[i]]
                for i, _ in enumerate(list_)]

    @classmethod
    def from_list(cls, list_, length):
        indices_after = deque(range(length))
        program_swaps_after = deque(ascii_lowercase[:length])
        for move in list_:
            f = partial_function_from_string(move)
            if move[0] in {'s', 'x'}:
                indices_after = f(indices_after)
            else:
                program_swaps_after = f(program_swaps_after)
        return cls(indices_after, program_swaps_after)


if __name__ == '__main__':
    input_ = input_list(16)
    output = ''.join(dance(deque('abcdefghijklmnop'), input_))
    print(output)

    translator = TranslatorFactory(1000000000).create_repeated_translators(
        input_, 16)
    print(''.join(translator.translate('abcdefghijklmnop')))
