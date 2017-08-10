

import unittest
from pyfunctory.factories import match_compose, juxt_compose


class MatchComposeTest(unittest.TestCase):
    def setUp(self):
        self.nums = [1, 2, 101, 4, 102, 6]
        self.is_even = lambda x: x % 2 == 0
        self.small = lambda x: x < 100

    def test_all_match_compose(self):
        comp_func = match_compose(self.is_even, self.small)
        self.assertListEqual([x for x in self.nums if comp_func(x)], [2, 4, 6])

    def test_any_match_compose(self):
        comp_func = match_compose(self.is_even, self.small, func=any)
        self.assertListEqual([x for x in self.nums if comp_func(x)], [1, 2, 4, 102, 6])

    def test_all_false_match_compose(self):
        comp_func = match_compose(self.is_even, self.small, match=False)
        self.assertListEqual([x for x in self.nums if comp_func(x)], [1, 101, 102])

    def test_any_false_match_compose(self):
        comp_func = match_compose(self.is_even, self.small, func=any, match=False)
        self.assertListEqual([x for x in self.nums if comp_func(x)], [101])


class JuxtComposeTest(unittest.TestCase):
    def setUp(self):
        def bulk_rate(price):
            return price - (price * 0.1)
        def fixed_lump(price):
            return price - 10.0
        def new_special(price):
            price = price - (price * 0.05)
            return price - 5
        self.bulk_rate = bulk_rate
        self.fixed_lump = fixed_lump
        self.new_special = new_special

    def test_basic_juxtapose(self):
        toilet_paper = 20
        bargain_analysis = juxt_compose(self.bulk_rate, self.fixed_lump, self.new_special)
        self.assertEqual(bargain_analysis(toilet_paper), (18.0, 10.0, 14.0))


if __name__ == '__main__':
    unittest.main()
