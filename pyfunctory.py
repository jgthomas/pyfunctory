

import functools
import operator


"""
ATOMS

Small, self-contained functions providing boolean 
tests and basic operations.

Many are provided by the operator module:

"""

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



"""
NUGGETS

"""



"""
UTILITIES

"""



""""
PROCESSES

"""
def feed_filter(feed, criterion=None, *comparison):
    for element in feed:
        element = element.strip()
        if criterion:
            if not criterion(element, *comparison):
                continue
        if not element:
            continue
        yield element


def load_words(word_file, criterion=None, *comparison):
    with open(word_file) as filename:
        return [word for word
                in feed_filter(filename, criterion, *comparison)]


def data_filter(data, criterion=None, *comparison):
    return [element for element
            in feed_filter(data, criterion, *comparison)]



"""
FACTORIES

Higher-order functions for the creation of other functions, 
generators and larger program flow sequences.

"""
def make_partial(func, *args, **kwargs):
    return functools.partial(func, *args, **kwargs)


def compose(*funcs):
    def inner(data, funcs=funcs):
        result = data
        for f in funcs:
            result = f(result)
        return result
    return inner
