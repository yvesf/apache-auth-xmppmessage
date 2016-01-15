#!/usr/bin/env python3
import unittest
import login


class TestStringMethods(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(login.normalize_token("A4-B4-C5"),
            "A4B4C5")
        self.assertEqual(login.normalize_token("a4-b4-c5"),
            "A4B4C5")
        self.assertEqual(login.normalize_token("a4b4c5"),
            "A4B4C5")
        self.assertEqual(login.normalize_token("A4B4C5"),
            "A4B4C5")


if __name__ == '__main__':
    unittest.main()
