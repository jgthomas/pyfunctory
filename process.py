""""
PROCESS

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


def load_data(data_file, criterion=None, *comparison):
    with open(data_file) as filename:
        return [line for line
                in feed_filter(filename, criterion, *comparison)]


def filter_data(data, criterion=None, *comparison):
    return [element for element
            in feed_filter(data, criterion, *comparison)]
