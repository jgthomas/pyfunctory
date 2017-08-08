"""
COMPOUNDS

More complex comparison functions.

"""


def can_be_made(ref, item, exact_match=False):
    """
    Test if one iterable can be made from elements in another.

    Considers both element type, and token frequency.

    Args:
        ref (iterable): basis for comparison
        item (iterable): item to be compared with reference
        exact_match (bool): if True, *every* element in each
                    iterable must have a matching element in the
                    other iterable, otherwise item need only match
                    a subset of ref

    Returns:
        bool: True if can be made, otherwise False.

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
