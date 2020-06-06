
from pyfunctory.compounds import can_be_made


def test_same_length_string():
    assert can_be_made("pots", "stop") == True

def test_exact_same_length_string():
    assert can_be_made("pots", "stop", exact_match=True) == True

def test_different_length_string():
    assert can_be_made("poster", "stop") == True

def test_double_letter_both():
    assert can_be_made("posters", "stops") == True

def test_double_letter_in_reference():
    assert can_be_made("bassoon", "bas") == True

def test_two_double_letters_in_reference():
    assert can_be_made("decorator", "doctor") == True

def test_three_double_letters_in_reference():
    assert can_be_made("diskettes", "diskett") == True

def test_integers_same_length():
    reference = (1, 2, 3, 4)
    test = (2, 3, 4, 1)
    assert can_be_made(reference, test) == True

def test_exact_integers_same_length():
    reference = (1, 2, 3, 4)
    item = (2, 3, 4, 1)
    assert can_be_made(reference, item, exact_match=True) == True

def test_same_length_list():
    reference = ["p", "o", "t", "s"]
    item = ["s", "t", "o", "p"]
    assert can_be_made(reference, item) == True

def test_exact_same_length_list():
    reference = ["p", "o", "t", "s"]
    item = ["s", "t", "o", "p"]
    assert can_be_made(reference, item, exact_match=True) == True

def test_different_length_list():
    reference = ["p", "o", "t", "s", "e", "r"]
    item = ["s", "t", "o", "p"]
    assert can_be_made(reference, item) == True

def test_mixed_element_types():
    reference = (1, 2, 3, 4, "a", "b", 1.2)
    item = (2, 3, 4, 1, "a", 1.2)
    assert can_be_made(reference, item) == True

def test_word():
    reference = ["happy", "birthday", "to", "you"]
    item = ["happy", "birthday"]
    assert can_be_made(reference, item) == True

def test_variables():
    a = "dog"
    b = "cat"
    c = "man"
    reference = [a, b, c]
    item = [a, b]
    assert can_be_made(reference, item) == True

def test_same_length_string_fail():
    assert can_be_made("pott", "stop") == False

def test_different_length_string_fail():
    assert can_be_made("poter", "stop") == False

def test_exact_different_length_string():
    assert can_be_made("poster", "stop", exact_match=True) == False

def test_same_letters_different_amounts():
    assert can_be_made("settee", "tsetse") == False

def test_exact_same_letters_different_amounts():
    assert can_be_made("settee", "tsetse", exact_match=True) == False

def test_item_longer_than_ref():
    assert can_be_made("poster", "stopper") == False

def test_double_letter_in_item():
    assert can_be_made("basoon", "bass") == False

def test_two_double_letters_in_item():
    assert can_be_made("basoons", "baboons") == False

def test_three_double_letters_in_item():
    assert can_be_made("abcdefg", "aabbccd") == False

def test_exact_different_length_list():
    reference = ["p", "o", "t", "s", "e", "r"]
    item = ["s", "t", "o", "p"]
    assert can_be_made(reference, item, exact_match=True) == False

def test_test_longer_than_reference():
    reference = ["p", "o", "t", "s", "e", "r"]
    item = ["s", "t", "o", "p", "i", "m", "e", "r"]
    assert can_be_made(reference, item) == False

def test_exact_test_longer_than_reference():
    reference = ["p", "o", "t", "s", "e", "r"]
    item = ["s", "t", "o", "p", "i", "m", "e", "r"]
    assert can_be_made(reference, item, exact_match=True) == False

def test_exact_mixed_element_types():
    reference = (1, 2, 3, 4, "a", "b", 1.2)
    item = (2, 3, 4, 1, "a", 1.2)
    assert can_be_made(reference, item, exact_match=True) == False

def test_exact_word():
    reference = ["happy", "birthday", "to", "you"]
    item = ["happy", "birthday"]
    assert can_be_made(reference, item, exact_match=True) == False

def test_variables_fail():
    a = "dog"
    b = "cat"
    c = "man"
    d = "monkey"
    reference = [a, b, c]
    item = [a, b, d]
    assert can_be_made(reference, item) == False

def test_exact_variables():
    a = "dog"
    b = "cat"
    c = "man"
    reference = [a, b, c]
    item = [a, b]
    assert can_be_made(reference, item, exact_match=True) == False
