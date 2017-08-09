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

    >>> types_a = (1, 2, 3, 4)
    >>> types_b = (1, 2, 3, 5, 6)
    >>> can_be_made(types_a, types_b)
    False
    >>> can_be_made(types_b, types_a)
    False

    >>> tokens_a = ("a", "b", "c", "d")
    >>> tokens_b = ("a", "a", "b", "c", "d")
    >>> can_be_made(tokens_a, tokens_b)
    False
    >>> can_be_made(tokens_b, tokens_a)
    True

    """
    if exact_match:
        if len(item) != len(ref):
            return False
    else:
        if len(item) > len(ref):
            return False

    overlap_tokens = [e for e in ref if e not in set(ref).difference(item)]
    if len(overlap_tokens) < len(item):
        return False

    overlap_types = sorted(set(str(e) for e in overlap_tokens))
    if len(overlap_types) != len(set(item)):
        return False

    item_freqs = (item.count(e) for e in overlap_types)
    overlap_freqs = (overlap_tokens.count(e) for e in overlap_types)
    elements_match = (True if overlap_freq - item_freq >= 0 else False
                      for overlap_freq, item_freq
                      in zip(overlap_freqs, item_freqs))
    return all(elements_match)



#def can_be_made(ref, item, exact_match=False):
#    """
#    Test if one iterable can be made from elements in another.
#
#    Args:
#        ref (iterable): basis for comparison
#        item (iterable): item to be compared with ref
#        exact_match (bool): if True, *every* element in each
#                    iterable must have a matching element in the
#                    other iterable, otherwise item need only match
#                    a subset of ref
#
#    Returns:
#        bool: True if can be made, otherwise False.
#
#    Iterables can differ both in the 'types' (or set) of elements they
#    contain and in the frequency of the 'tokens' of those types.
#
#    >>> types_a = (1, 2, 3, 4)
#    >>> types_b = (1, 2, 3, 5, 6)
#    >>> can_be_made(types_a, types_b)
#    False
#    >>> can_be_made(types_b, types_a)
#    False
#
#    >>> tokens_a = ("a", "b", "c", "d")
#    >>> tokens_b = ("a", "a", "b", "c", "d")
#    >>> can_be_made(tokens_a, tokens_b)
#    False
#    >>> can_be_made(tokens_b, tokens_a)
#    True
#
#    """
#    if exact_match:
#        if len(item) != len(ref):
#            return False
#
#    overlap = [e for e in ref if e not in set(ref).difference(item)]
#
#    if len(overlap) < len(item):
#        return False
#
#    def to_chars(x):
#        return [str(e) for e in x]
#
#    if (sorted(to_chars(item)) == sorted(to_chars(overlap))
#        or len(item) == len(set(overlap))):
#        return True
#    return False
