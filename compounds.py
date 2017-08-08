"""
COMPOUNDS

"""


def can_be_made(ref, item, exact_match=False):
    """
    Test if one iterable can be made from elements in another.

    Args:
        ref (iterable): basis for comparison
        item (iterable): item to be compared with ref
        exact_match (bool): if True, *every* element in each
                    iterable must have a matching element in the
                    other iterable, otherwise item need only match
                    a subset of ref

    Returns:
        bool: True if can be made, otherwise False.

    Iterables can differ both in the 'types' (or set) of elements they
    contain and in the frequency of the 'tokens' of those types.

    >>> a = (1, 2, 3, 4)
    >>> b = (1, 2, 3, 5, 6)
    >>> can_be_made(a, b)
    False
    >>> can_be_made(b, a)
    False

    >>> a = ("a", "b", "c", "d")
    >>> b = ("a", "a", "b", "c", "d")
    >>> can_be_made(a, b)
    False
    >>> can_be_made(b, a)
    True

    """
    if exact_match:
        if len(item) != len(ref):
            return False

    if not set(item).issubset(ref):
        return False

    def to_chars(x):
        return [str(e) for e in x]

    overlap = [e for e in ref if e not in set(ref).difference(item)]

    if (sorted(to_chars(item)) == sorted(to_chars(overlap))
        or len(item) == len(set(overlap))):
        return True
    return False
