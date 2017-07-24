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
    >>> contains_e = make_partial(contains, "e")

    >>> add2(10)
    12
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


def map_over(func):
    """
    Return generator that applies func to all elements.

    Works like map.

    >>> nums = [1, 2, 3, 4]
    >>> import operator
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


def map_over_filter_by(map_func, filter_func):
    """
    Return generator that maps a function only to those
    elements filtered by some criteria, leaving the other
    elements intact.

    >>> nums = [1, 2, 3, 4, 5]
    >>> import operator
    >>> is_odd = lambda x: x % 2 != 0
    >>> add100 = make_partial(operator.add, 100)

    >>> add_100_to_odd = map_over_filter_by(add100, is_odd)
    >>> list(add_100_to_odd(nums))
    [101, 2, 103, 4, 105]

    """
    def generator(data):
        return (map_func(x) if filter_func(x) else x for x in data)
    return generator
