"""
FACTORIES

"""


import functools
import itertools
import operator
from pyfunctory.utilities import juxt


def make_partial(func, *args, **kwargs):
    """
    Return partially applied function for use in pipelines.

    >>> import operator
    >>> from atoms import contains

    >>> add2 = make_partial(operator.add, 2)
    >>> add2(10)
    12
    >>> contains_e = make_partial(contains, "e")
    >>> contains_e("help")
    True
    >>> contains_e("batman")
    False

    """
    return functools.partial(func, *args, **kwargs)


def compose(*funcs):
    """
    Return a function that applies all the supplied functions to the data.

    >>> import operator
    >>> add2 = make_partial(operator.add, 2)
    >>> mul3 = make_partial(operator.mul, 3)

    >>> add2_then_mul3 = compose(add2, mul3)
    >>> add2_then_mul3(6)
    24

    """
    def inner(data, funcs=funcs):
        result = data
        for f in funcs:
            result = f(result)
        return result
    return inner


def match_compose(*tests, func=all, match=True):
    """
    Return function to run series of tests on an input.

    tests  :  series of single-argument Boolean functions
    func   :  overall evaluation to apply: all, any
    match  :  whether tests should pass if True or False

    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> is_odd = lambda x: x % 2 != 0
    >>> over_3 = lambda x: x > 3

    >>> test1 = match_compose(is_odd, over_3)
    >>> [n for n in nums if test1(n)]
    [5, 7, 9]

    >>> test2 = match_compose(is_odd, over_3, func=any)
    >>> [n for n in nums if test2(n)]
    [1, 3, 4, 5, 6, 7, 8, 9]

    >>> test3 = match_compose(is_odd, over_3, match=False)
    >>> [n for n in nums if test3(n)]
    [1, 2, 3, 4, 6, 8]

    >>> test4 = match_compose(is_odd, over_3, func=any, match=False)
    >>> [n for n in nums if test4(n)]
    [2]

    """
    def is_match(x):
        return func(t(x) for t in tests)
    def is_not_match(x):
        return not func(t(x) for t in tests)
    return is_match if match else is_not_match


def juxt_compose(*funcs, reducer=None):
    """
    Return tuple of each func result, or a reduction of those results.

    funcs    :  series of one-argument functions
    reducer  :  optional reducing function

    >>> add2 = lambda x: x + 2
    >>> mul3 = lambda x: x * 3
    >>> pow4 = lambda x: x ** 4

    >>> test1 = juxt_compose(add2, mul3, pow4)
    >>> test1(5)
    (7, 15, 625)

    >>> test2 = juxt_compose(add2, mul3, pow4, reducer=max)
    >>> test2(5)
    625

    >>> nums = [3, 4, 5]

    >>> test3 = juxt_compose(add2, mul3, pow4)
    >>> [test3(x) for x in nums]
    [(5, 9, 81), (6, 12, 256), (7, 15, 625)]

    >>> test4 = juxt_compose(add2, mul3, pow4, reducer=min)
    >>> [test4(x) for x in nums]
    [5, 6, 7]

    """
    def identity(x):
        return x

    if reducer is None:
        reducer = identity

    def inner(x):
        return reducer(juxt(x, *funcs))
    return inner


def map_over(func):
    """
    Return generator that applies func to all elements.

    >>> import operator
    >>> nums = [1, 2, 3, 4]
    >>> add3 = make_partial(operator.add, 3)

    >>> add_three = map_over(add3)
    >>> list(add_three(nums))
    [4, 5, 6, 7]

    """
    def generator(data):
        return (func(x) for x in data)
    return generator


def filter_by(func):
    """
    Return generator that filters all elements by func.

    >>> nums = [1, 2, 3, 4, 5]
    >>> is_odd = lambda x: x % 2 != 0

    >>> odd = filter_by(is_odd)
    >>> list(odd(nums))
    [1, 3, 5]

    """
    def generator(data):
        return (x for x in data if func(x))
    return generator


def reduce_to(reducer, func=None):
    if not func:
        func = operator.add
    def generator(data):
        return reducer(itertools.accumulate(data, func))
    return generator


def map_filtered(map_func, filter_func, remove=False):
    """
    Return generator that maps a function only to those
    elements filtered by some criteria.

    If remove is set to True, elements that don't match the
    filter are deleted, otherwise they pass through unchanged.

    >>> nums = [1, 2, 3, 4, 5]
    >>> is_odd = lambda x: x % 2 != 0
    >>> add100 = lambda x: x + 100

    >>> add_100_to_odd = map_filtered(add100, is_odd)
    >>> list(add_100_to_odd(nums))
    [101, 2, 103, 4, 105]

    >>> add_100_to_odd = map_filtered(add100, is_odd, remove=True)
    >>> list(add_100_to_odd(nums))
    [101, 103, 105]

    """
    def generator(data):
        if remove:
            return (map_func(x) for x in data if filter_func(x))
        return (map_func(x) if filter_func(x) else x for x in data)
    return generator
