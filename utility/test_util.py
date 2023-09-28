"""Test utility functions. 
"""

import unittest

import util


class TestUtil(unittest.TestCase):
    def test_sub_int(self):
        self.assertEqual(util.sub(1, 2), -1)

    def test_sub_float(self):
        self.assertEqual(util.sub(1.0, 2.0), -1.0)
