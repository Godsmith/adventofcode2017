from day4 import is_valid_passphrase, is_anagram


def test_is_anagram():
    assert is_anagram('hello', 'elloh')
    assert not is_anagram('eello', 'elloh')

def test_is_valid_passphrase():
    assert is_valid_passphrase('abcde fghij'.split())
    assert not is_valid_passphrase('abcde xyz ecdab'.split())
    assert is_valid_passphrase('iiii oiii ooii oooi oooo'.split())
    assert not is_valid_passphrase('oiii ioii iioi iiio'.split())
