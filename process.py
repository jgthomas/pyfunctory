""""
PROCESS

Functions for the processing of streams, files and other sequences of data.

"""


def feed_filter(feed, criterion=None, *comparison):
    """
    Return a filtered stream of elements.

    feed       :  file, list, tuple, or other data source
    criterion  :  function that filters elements of the feed
    comparison :  comparator against which element is checked

    Comparison is optional as some criteria, such as is_palindrome,
    do not require a second factor to compare against

    If no criteron function is supplied, returns all elements.

    """
    for element in feed:
        element = element.strip()
        if criterion:
            if not criterion(element, *comparison):
                continue
        if not element:
            continue
        yield element


def load_data(data_file, criterion=None, *comparison):
    """ Run feed_filter over a file. """
    with open(data_file) as filename:
        return [line for line
                in feed_filter(filename, criterion, *comparison)]


def filter_data(data, criterion=None, *comparison):
    """ Run feed_filter over sequence data type. """
    return [element for element
            in feed_filter(data, criterion, *comparison)]
