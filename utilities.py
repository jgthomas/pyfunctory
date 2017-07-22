"""
UTILITIES

Small, functional-style utilites.

"""


import functools
import itertools


def take(n, iterator):
    """ Return the first n elements. """
    return itertools.islice(iterator, n)


def drop(n, it):
    """ Return all but the first n elements """
    return itertools.islice(it, n, None)


def tail(it):
    """ Return all but the first element. """
    t = functools.partial(drop, 1)
    return t(it)


def iterate(f, x):
    """
    Applies f to x, then f(f(x)), then f(f(f(x))), etc.

    Example: apply double three times to an x of 2
    >>> double = lambda x: x + x
    >>> take(4, iterate(double, 2))
    [2, 4, 8, 16]

    """
    return itertools.accumulate(itertools.repeat(x), lambda fx, _: f(fx))
