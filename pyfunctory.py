

import functools
import operator
import re


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

    Membership
    contains  :  in (x in y)
    is        :  is (x is y)
    is_not    :  (x is not y)

In all cases, the comparison is added first to fascilitate partial application.

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


"""
COMPARISONS

Longer, more complex comparison functions.

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

Regex patterns for filtering purposes.

"""
initial_lowercase = re.compile(r'^[a-z]')

initial_capital = re.compile(r'^[A-Z]')

all_lower = re.compile(r'^[a-z]+$')

all_upper = re.compile(r'^[A-Z]+$')

all_word_chars = re.compile(r'\w+$')

all_non_word_chars = re.compile(r'\W+$')

ends_ss = re.compile(r'^[A-Za-z]+ss$')


"""
UTILITIES

Small, functional-style utilites.

"""
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


""""
PROCESSES

Functions for the processing of streams, files and other sequences of data.

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
generators and larger program-flow sequences.

"""
def make_partial(func, *args, **kwargs):
    """
    Return partially applied function for use in pipelines.

    Example:
    >>> add2 = make_partial(operator.add, 2)
    >>> add2(10)
    >>> 12

    """
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
