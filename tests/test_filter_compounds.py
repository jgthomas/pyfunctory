

import unittest
from pyfunctory.filter_compounds import can_be_made


class CanBeMadeTrue(unittest.TestCase):
    def test_same_length_string(self):
        self.assertIs(can_be_made("pots", "stop"), True)
      
    def test_exact_same_length_string(self):
        self.assertIs(can_be_made("pots", "stop", exact_match=True), True)
      
    def test_different_length_string(self):
        self.assertIs(can_be_made("poster", "stop"), True)

    def test_double_letter(self):
        self.assertIs(can_be_made("posters", "stops"), True)
    
    def test_integers_same_length(self):
        reference = (1, 2, 3, 4)
        test = (2, 3, 4, 1)
        self.assertIs(can_be_made(reference, test), True)
      
    def test_exact_integers_same_length(self):
        reference = (1, 2, 3, 4)
        item = (2, 3, 4, 1)
        self.assertIs(can_be_made(reference, item, exact_match=True), True)
      
    def test_same_length_list(self):
        reference = ["p", "o", "t", "s"]
        item = ["s", "t", "o", "p"]
        self.assertIs(can_be_made(reference, item), True)
    
    def test_exact_same_length_list(self):
        reference = ["p", "o", "t", "s"]
        item = ["s", "t", "o", "p"]
        self.assertIs(can_be_made(reference, item, exact_match=True), True)
      
    def test_different_length_list(self):
        reference = ["p", "o", "t", "s", "e", "r"]
        item = ["s", "t", "o", "p"]
        self.assertIs(can_be_made(reference, item), True)
      
    def test_mixed_element_types(self):
        reference = (1, 2, 3, 4, "a", "b", 1.2)
        item = (2, 3, 4, 1, "a", 1.2)
        self.assertIs(can_be_made(reference, item), True)
      
    def test_word(self):
        reference = ["happy", "birthday", "to", "you"]
        item = ["happy", "birthday"]
        self.assertIs(can_be_made(reference, item), True)
    
    def test_variables(self):
        a = "dog"
        b = "cat"
        c = "man"
        reference = [a, b, c]
        item = [a, b]
        self.assertIs(can_be_made(reference, item), True)
      
    def test_exact_variables(self):
        a = "dog"
        b = "cat"
        c = "man"
        reference = [a, b, c]
        item = [a, b]
        self.assertIs(can_be_made(reference, item, exact_match=True), False)
      
  
class CanBeMadeFalse(unittest.TestCase):
    def test_same_length_string_fail(self):
        self.assertIs(can_be_made("pott", "stop"), False)
      
    def test_different_length_string_fail(self):
        self.assertIs(can_be_made("poter", "stop"), False)
      
    def test_exact_different_length_string(self):
        self.assertIs(can_be_made("poster", "stop", exact_match=True), False)
      
    def test_same_letters_different_amounts(self):
        self.assertIs(can_be_made("settee", "tsetse"), False)
      
    def test_exact_same_letters_different_amounts(self):
        self.assertIs(can_be_made("settee", "tsetse", exact_match=True), False)
      
    def test_exact_different_length_list(self):
        reference = ["p", "o", "t", "s", "e", "r"]
        item = ["s", "t", "o", "p"]
        self.assertIs(can_be_made(reference, item, exact_match=True), False)
      
    def test_test_longer_than_reference(self):
        reference = ["p", "o", "t", "s", "e", "r"]
        item = ["s", "t", "o", "p", "i", "m", "e", "r"]
        self.assertIs(can_be_made(reference, item), False)
    
    def test_exact_test_longer_than_reference(self):
        reference = ["p", "o", "t", "s", "e", "r"]
        item = ["s", "t", "o", "p", "i", "m", "e", "r"]
        self.assertIs(can_be_made(reference, item, exact_match=True), False)
      
    def test_exact_mixed_element_types(self):
        reference = (1, 2, 3, 4, "a", "b", 1.2)
        item = (2, 3, 4, 1, "a", 1.2)
        self.assertIs(can_be_made(reference, item, exact_match=True), False)
      
    def test_exact_word(self):
        reference = ["happy", "birthday", "to", "you"]
        item = ["happy", "birthday"]
        self.assertIs(can_be_made(reference, item, exact_match=True), False)
      
    def test_variables_fail(self):
        a = "dog"
        b = "cat"
        c = "man"
        d = "monkey"
        reference = [a, b, c]
        item = [a, b, d]
        self.assertIs(can_be_made(reference, item), False)
      

if __name__ == '__main__':
    unittest.main()
