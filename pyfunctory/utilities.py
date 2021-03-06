"""
UTILITIES

Small, functional-style utilites.

"""


import functools
import itertools


def take(n, iterator):
    """ Return the first n elements. """
    return itertools.islice(iterator, n)


def drop(n, iterator):
    """ Return all but the first n elements """
    return itertools.islice(iterator, n, None)


def tail(iterator):
    """ Return all but the first element. """
    t = functools.partial(drop, 1)
    return t(iterator)


def iterate(f, x):
    """
    Applies f to x, then f(f(x)), then f(f(f(x))), etc.

    >>> double = lambda x: x + x
    >>> list(take(4, iterate(double, 2)))
    [2, 4, 8, 16]
    >>> max(take(4, iterate(double, 2)))
    16

    """
    return itertools.accumulate(itertools.repeat(x), lambda fx, _: f(fx))


def pipe(data, *funcs):
    """
    Send data through a series of functions, returning final output.

    Requires functions which take a single argument.

    >>> double = lambda x: x * 2
    >>> pipe(6, double, str, double)
    '1212'

    """
    for func in funcs:
        data = func(data)
    return data


def juxt(x, *funcs):
    """
    Return tuple of each func applied to x.

    >>> add2 = lambda x: x + 2
    >>> mulby3 = lambda x: x * 3
    >>> pow2 = lambda x: x ** 2
    >>> juxt(10, add2, mulby3, pow2)
    (12, 30, 100)

    """
    return tuple(func(x) for func in funcs)
