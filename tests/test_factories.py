

import unittest
from pyfunctory.factories import match_compose


class MatchComposeTest(unittest.TestCase):
    def test_all_match_compose(self):
        nums = [1, 2, 101, 4, 102, 6]
        is_even = lambda x: x % 2 == 0
        small = lambda x: x < 100
        comp_func = match_compose(is_even, small)
        self.assertListEqual([x for x in nums if comp_func(x)], [2, 4, 6])

    def test_any_match_compose(self):
        nums = [1, 2, 101, 4, 102, 6]
        is_even = lambda x: x % 2 == 0
        small = lambda x: x < 100
        comp_func = match_compose(is_even, small, func=any)
        self.assertListEqual([x for x in nums if comp_func(x)], [1, 2, 4, 102, 6])

    def test_all_false_match_compose(self):
        nums = [1, 2, 101, 4, 102, 6]
        is_even = lambda x: x % 2 == 0
        small = lambda x: x < 100
        comp_func = match_compose(is_even, small, match=False)
        self.assertListEqual([x for x in nums if comp_func(x)], [1, 101, 102])

    def test_any_false_match_compose(self):
        nums = [1, 2, 101, 4, 102, 6]
        is_even = lambda x: x % 2 == 0
        small = lambda x: x < 100
        comp_func = match_compose(is_even, small, func=any, match=False)
        self.assertListEqual([x for x in nums if comp_func(x)], [101])


if __name__ == '__main__':
    unittest.main()
