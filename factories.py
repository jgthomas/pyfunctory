"""
FACTORIES

Higher-order functions for the creation of other functions, 
generators and larger program-flow sequences.

"""


import functools


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


def is_true(*tests):
    """
    Return True if all tests pass.

    Tests can be single-argument functions or compiled regex patterns.

    Works like compose but for filters.

    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> is_odd = lambda x: x % 2 != 0
    >>> over_3 = lambda x: x > 3

    >>> test = is_true(is_odd, over_3)
    >>> [n for n in nums if test(n)]
    [5, 7, 9]

    >>> import re
    >>> words = ["awe", "hiss", "ass", "pass", "piss", "kiss"]
    >>> start_p = lambda x: x[0] == "p"
    >>> ends_ss = re.compile(r'^[A-Za-z]+ss$')

    >>> test2 = is_true(start_p, ends_ss)
    >>> [word for word in words if test2(word)]
    ['pass', 'piss']

    """
    def tester(x):
        for test in tests:
            try:
                if test(x):
                    continue
            except TypeError:
                if test.match(x):
                    continue
            return False
        return True
    return tester


#def all_match(*tests, match=True):
#    def is_match(x):
#        return all(p(x) for p in tests)
#    def is_not_match(x):
#        return not all(p(x) for p in tests)
#    if match:
#        return is_match
#    return is_not_match
#
#
#def any_match(*tests, match=True):
#    def is_match(x):
#        return any(p(x) for p in tests)
#    def is_not_match(x):
#        return not any(p(x) for p in tests)
#    if match:
#        return is_match
#    return is_not_match

def flip(func, a, b):
    return func(b, a)

def simple_juxt(x, *funcs):
    return tuple(func(x) for func in funcs)

def juxt(*funcs):
    def tester(x):
        return tuple(func(x) for func in funcs)
    return tester


def map_over(func):
    """
    Return generator that applies func to all elements.

    Works like map.

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

    Works like filter.

    >>> nums = [1, 2, 3, 4, 5]
    >>> is_odd = lambda x: x % 2 != 0

    >>> odd = filter_by(is_odd)
    >>> list(odd(nums))
    [1, 3, 5]

    """
    def generator(data):
        return (x for x in data if func(x))
    return generator


def map_filtered(map_func, filter_func, remove=False):
    """
    Return generator that maps a function only to those
    elements filtered by some criteria.

    If remove is set to True, elements that don't match the
    filter are deleted, otherwise they pass through unchanged.

    >>> import operator
    >>> nums = [1, 2, 3, 4, 5]
    >>> is_odd = lambda x: x % 2 != 0
    >>> add100 = make_partial(operator.add, 100)

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
