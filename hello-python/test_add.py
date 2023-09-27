import unittest

import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add.add(1, 2), 3)
        self.assertEqual(add.add(1, -1), 0)
