"""
NUGGETS

Regex patterns for filtering purposes.

"""


import re


ini_lower = re.compile(r'^[a-z]')

ini_upper = re.compile(r'^[A-Z]')

all_lower = re.compile(r'^[a-z]+$')

all_upper = re.compile(r'^[A-Z]+$')

all_word_chars = re.compile(r'\w+$')

all_non_word_chars = re.compile(r'\W+$')

ends_ss = re.compile(r'^[A-Za-z]+ss$')


def match_factory(*nuggets, match=True):
    """ Return function to test item against all specified regex patterns. """
    def regex_match(item):
        """
        Return True if item matches all nuggets.

        i.e. one failed match will result in it returning False.

        Example:
        >>> match = match_factory(ini_cap, all_word_chars)
        >>> match("Dog")
        >>> True
        >>> match("Dog1")
        >>> False
        >>> match("dog")
        >>> False
        >>> match("dog1")
        >>> False
        """
        for nugget in nuggets:
            if nugget.match(item):
                continue
            else:
                return False
        return True
    def regex_not_match(item):
        """
        Return True if item does NOT match all nuggets.

        i.e. one successful match will result in it returning False

        Example:
        >>> not_match = match_factory(ini_cap, all_word_chars, match=False)
        >>> not_match("Dog")
        >>> False
        >>> not_match("Dog1")
        >>> False
        >>> not_match("dog")
        >>> False
        >>> not_match("dog1")
        >>> True

        """
        for nugget in nuggets:
            if not nugget.match(item):
                continue
            else:
                return False
        return True
    if match:
        return regex_match
    return regex_not_match
