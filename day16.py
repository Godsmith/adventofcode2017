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


def create_inverse_index_translation_list(before, after):
    tuples = ((i, after.index(b))
              for i, (b, a) in enumerate(zip(before, after)))
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    return [x[0] for x in sorted_tuples]


class TranslatorFactory:
    def __init__(self):
        self.translator_from_iterations = None

    def create_repeated_translators(self, list_, length, iterations):
        self.translator_from_iterations = {1: Translator.from_list(list_,
                                                                   length)}
        while self.maximum_translator_iterations() < iterations:
            largest_translator = self.translator_from_iterations[
                self.maximum_translator_iterations()]
            translator, size = self.largest_translator_that_fits(iterations)
            combined_translator = translator + largest_translator
            self.translator_from_iterations[
                self.maximum_translator_iterations() + size] = combined_translator
            print(self.maximum_translator_iterations())
        return combined_translator

    def largest_translator_that_fits(self, iterations):
        for size in reversed(sorted(self.translator_from_iterations.keys())):
            if self.maximum_translator_iterations() + size <= iterations:
                return self.translator_from_iterations[size], size

    def create_translator(self, indices_after, program_swaps_after):
        """Creates a translator function with certain properties.

        :arg indices_after:
        :arg program_swaps_after"""
        translations = create_inverse_index_translation_list(before, after)

        def translator(list_):
            return [list_[translations[i]] for i, _ in enumerate(list_)]

        return translator

    def maximum_translator_iterations(self):
        return max(self.translator_from_iterations)


class Translator:
    def __init__(self, indices_after, program_swaps_after):
        """Creates a translator with certain properties.

        :arg indices_after: The indices after swapping, e.g. 43210.
        :arg program_swaps_after: Dict with program translations,
        e.g. {'a': 'e', 'b': 'd', ...}.
        """
        self.indices_after = indices_after
        self.programs = {source: target for source, target in
                         zip(ascii_lowercase, program_swaps_after)}
        # TODO: remove
        self.index_translations = create_inverse_index_translation_list(
            range(len(indices_after)), indices_after)

    def __add__(self, other):
        new_indices_after = self._index_translate(other.indices_after)
        new_programs = self._program_swap(other.programs.values())
        return Translator(new_indices_after, new_programs)

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


def translate_repeatedly(f, input_, iterations):
    for _ in range(iterations):
        input_ = f(input_)
    return input_


if __name__ == '__main__':
    input_ = input_list(16)
    output = ''.join(dance(deque('abcdefghijklmnop'), input_))
    print(output)
    translator = TranslatorFactory().create_repeated_translators(input_, 16,
                                                                 1000000000)
    print(''.join(translator.translate('abcdefghijklmnop')))
