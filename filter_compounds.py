#def can_be_made(reference, item, exact_match=False):
#    """
#    Test if item can be made from elements in reference.
#
#    Considers both element type, and token frequency.
#
#    Args:
#        reference (iterable): basis for comparison
#        item (iterable): item to be compared with reference
#        exact_match (bool): if True, *every* element in each iterable must
#            have a matching element in the other iterable, otherwise
#            item need only match a subset of reference
#
#    Returns:
#        bool: True if can be made, otherwise False.
#
#    """
#    if exact_match:
#      if len(item) != len(reference):
#        return False
#
#    def to_chars(x):
#      return [str(e) for e in x]
#
#    overlap = [elem for elem in reference if elem in item]
#    return sorted(to_chars(item)) == sorted(to_chars(overlap))


def can_be_made(ref, item, exact_match=False):
    if exact_match:
        if len(item) != len(ref):
            return False

    def to_chars(x):
        return [str(e) for e in x]

    overlap = list(x for x in ref if x not in set(ref).difference(item))

    if (sorted(to_chars(item)) == sorted(to_chars(overlap))
        or len(item) == len(set(overlap))):
        return True
    return False
