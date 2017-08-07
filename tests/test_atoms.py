

import unittest

from pyfunctory.atoms import is_palindrome


class PalindromeTest(unittest.TestCase):
    def test_lowercase_palindrome(self):
        self.assertIs(is_palindrome('atta'), True)

    def test_uppercase_palindrome(self):
        self.assertIs(is_palindrome('OTTO'), True)

    def test_mixedcase_palindrome(self):
        self.assertIs(is_palindrome('ObTTbO'), True)

    def test_nonpalindrome_lower(self):
        self.assertIs(is_palindrome('wghysg'), False)

    def test_nonpalindrome_upper(self):
        self.assertIs(is_palindrome('HHRGKIUHN'), False)

    def test_nonpalindrome_mixed(self):
        self.assertIs(is_palindrome('hRGiUhN'), False)

    def test_number_string_palindrome(self):
        self.assertIs(is_palindrome('123321'), True)

    def test_number_string_nonpalindrome(self):
        self.assertIs(is_palindrome('23321'), False)

    def test_number_letter_mix_palindrome(self):
        self.assertIs(is_palindrome('1f23g32f1'), True)

    def test_number_letter_mix_nonpalindrome(self):
        self.assertIs(is_palindrome('wfsa23w321'), False)

    def test_spaced_palindrome(self):
        self.assertIs(is_palindrome('a b c b a'), True)

    def test_uneven_spaced_palindrome(self):
        self.assertIs(is_palindrome('ab c b a'), True)
      
    def test_spaced_nonpalindrome(self):
        self.assertIs(is_palindrome('a D c b a'), False)

    def test_sentence_palindrome(self):
        self.assertIs(is_palindrome('madam im adam'), True)

    def test_sentence_nonpalindrome(self):
        self.assertIs(is_palindrome('mdam im adam'), False)

    def test_sentence_with_punctuation_middle_palindrome(self):
        self.assertIs(is_palindrome("madam i'm adam"), True)

    def test_sentence_with_punctuation_end_palindrome(self):
        self.assertIs(is_palindrome("madam i'm adam."), True)


if __name__ == '__main__':
    unittest.main()
