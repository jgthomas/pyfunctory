"""
NUGGETS

Regex patterns for filtering purposes.

"""


import re


initial_lowercase = re.compile(r'^[a-z]')

initial_capital = re.compile(r'^[A-Z]')

all_lower = re.compile(r'^[a-z]+$')

all_upper = re.compile(r'^[A-Z]+$')

all_word_chars = re.compile(r'\w+$')

all_non_word_chars = re.compile(r'\W+$')

ends_ss = re.compile(r'^[A-Za-z]+ss$')
