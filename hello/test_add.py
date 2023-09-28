import unittest

import add


class TestAdd(unittest.TestCase):
    def test_add_int(self):
        self.assertEqual(add.add(1, 2), 3)
        self.assertEqual(add.add(1, -1), 0)

    def test_add_float(self):
        self.assertEqual(add.add(1.0, 2.0), 3.0)
