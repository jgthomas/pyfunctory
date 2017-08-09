"""
ATOMS

Small, self-contained functions, providing boolean tests of criteria.

In all cases, the comparison is added first to fascilitate partial application.

"""


def contains(y, x):
    """ Return True if x is found in y. """
    return y in x


def does_not_contain(y, x):
    """ Return True if x is NOT found in y. """
    return y not in x


def is_length(length, item):
    """ Return True if item is the specified length. """
    return len(item) == length


def longer_than(length, item):
    """ Return True if item is longer than specified length. """
    return len(item) > length


def shorter_than(length, item):
    """ Return True if item is shorter than specified length. """
    return len(item) < length


def starts_with(chars, string):
    """ Return True if string starts with specified characters. """
    chars = tuple(c.lower() for c in str(chars) if c.isalnum())
    return string.startswith(chars)


def ends_with(chars, string):
    """ Return True if string ends with specified characters. """
    chars = tuple(c.lower() for c in str(chars) if c.isalnum())
    return string.endswith(chars)


def is_palindrome(sequence):
    """ Return True if sequence is pallindromic. """
    clean_sequence = [c.lower() for c in str(sequence) if c.isalnum()]
    return clean_sequence == reversed(clean_sequence)


def char_set_size(set_size, item):
    """ Return True if item contains set_size unique elements. """
    return len(set(item)) == set_size


def contains_no(chars, item):
    """ Return True if item contains no instances of chars. """
    return set(item).isdisjoint(set(chars))


def no_repeats(item):
    """ Return True if there are no repeated elements. """
    return len(item) == len(set(item))


def is_subset(reference, item):
    """ Return True if item is a subset of reference. """
    return set(item).issubset(reference)
