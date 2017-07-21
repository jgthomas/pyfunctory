

import functools
import operator


"""
ATOMS

Small, self-contained functions, providing boolean tests and basic operations.

Many are provided by the operator module:
    
    Arithmetic
    add : add
    mul : multiply

    Comparative
    eq  : equal (==)
    ge  : greater than or equal (>=)
    gt  : greater than (>)
    le  : less than or equal (<=)
    lt  : less than (<)
    ne  : not equal (!=)


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


def map_over(func):
    """
    Return generator that applies func to all elements.

    Works like map.

    Example: generator to add 3 to every element
    >>> from operator import add
    >>> nums = [1, 2, 3, 4]
    >>> add3 = use_operator(add, 3)
    >>> add_three = map_over(add3)
    >>> nums_plus_three = (add_three(nums))
    >>> list(nums_plus_three)
    [4, 5, 6, 7]

    """
    def generator(data):
        return (func(x) for x in data)
    return generator


def filter_by(func):
    """
    Return generator that filters all elements by func.

    Works like filter.

    Example: return only odd numbers
    >>> is_odd = lambda x: x % 2 != 0
    >>> nums = [1, 2, 3, 4, 5]
    >>> odd = filter_by(is_odd)
    >>> odd_nums = (odd(nums))
    >>> list(odd_nums)
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

    Example: add 100 to all the odd numbers
    >>> from operator import add
    >>> is_odd = lambda x: x % 2 != 0
    >>> add100 = use_operator(add, 100)

    >>> nums = [1, 2, 3, 4, 5]
    
    >>> add_100_to_odd = map_over_filter_by(add100, is_odd)
    >>> odd_plus_100 = (add_100_to_odd(nums))
    >>> list(odd_plus_100)
    [101, 2, 103, 4, 105]

    """
    def generator(data):
        return (map_func(x) if filter_func(x) else x for x in data)
    return generator
