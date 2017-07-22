

import operator


"""
Small, self-contained functions, providing boolean tests and basic operations. 

These expand on the options found in the operator module. In all cases, the 
comparison is added first to fascilitate partial application.

"""
def does_not_contain(y, x):
    """ Return True if x is NOT found in y. """
    return not operator.contains(y, x)


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
    chars = tuple(c.lower() for c in chars)
    return string.startswith(chars)


def ends_with(chars, string):
    """ Return True if string ends with specified characters. """
    chars = tuple(c.lower() for c in chars)
    return string.endswith(chars)


def char_set_size(set_size, item):
    """ Return True if item contains set_size unique elements. """
    return len(set(item)) == set_size


def contains_no(chars, item):
    """ Return True if item contains no instances of chars. """
    return set(item).isdisjoint(set(chars))


def is_subset(reference, item):
    """ Return True if item is a subset of reference. """
    return set(item).issubset(reference)


def exact_match(x, y):
    """
    Return True if x is made of the same elements as y, including repeats.

    Examples:
    >>> exact_match("stop", "pots")
    >>> True
    >>> exact_match("settee", "tsetse")
    >>> False

    """
    return all(x_elem == y_elem for x_elem, y_elem in zip(sorted(x), sorted(y)))
