

from pyfunctory.atoms import is_palindrome


def test_lowercase_palindrome():
    assert is_palindrome('atta') == True

def test_uppercase_palindrome():
    assert is_palindrome('OTTO') == True

def test_mixedcase_palindrome():
    assert is_palindrome('ObTTbO') == True

def test_nonpalindrome_lower():
    assert is_palindrome('wghysg') == False

def test_nonpalindrome_upper():
    assert is_palindrome('HHRGKIUHN') == False

def test_nonpalindrome_mixed():
    assert is_palindrome('hRGiUhN') == False

def test_number_string_palindrome():
    assert is_palindrome('123321') == True

def test_number_string_nonpalindrome():
    assert is_palindrome('23321') == False

def test_number_letter_mix_palindrome():
    assert is_palindrome('1f23g32f1') == True

def test_number_letter_mix_nonpalindrome():
    assert is_palindrome('wfsa23w321') == False

def test_spaced_palindrome():
    assert is_palindrome('a b c b a') == True

def test_uneven_spaced_palindrome():
    assert is_palindrome('ab c b a') == True

def test_spaced_nonpalindrome():
    assert is_palindrome('a D c b a') == False

def test_sentence_palindrome():
    assert is_palindrome('madam im adam') == True

def test_sentence_nonpalindrome():
    assert is_palindrome('mdam im adam') == False

def test_sentence_with_punctuation_middle_palindrome():
    assert is_palindrome("madam i'm adam") == True

def test_sentence_with_punctuation_end_palindrome():
    assert is_palindrome("madam i'm adam.") == True
