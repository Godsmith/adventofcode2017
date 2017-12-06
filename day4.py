from util import input_lists
from itertools import product
from collections import Counter

print([len(set(list_)) == len(list_) for
       list_ in input_lists(4, ' ')].count(True))


def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)


def is_valid_passphrase(list_):
    for i, j in product(range(len(list_)), repeat=2):
        if i != j:
            if is_anagram(list_[i], list_[j]):
                return False
    return True


print([is_valid_passphrase(list_) for list_ in input_lists(4, ' ')].count(True))
