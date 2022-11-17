#!/usr/bin/python3
# Passing Test case for checking Limited Subtraction of numbers

import unittest
from Limited_Subtraction import LimitedSubtraction


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(LimitedSubtraction(-45, 23), 22)

    def testCase2(self):
        self.assertEqual(LimitedSubtraction(69, 23), 45)

    def testCase3(self):
        self.assertEqual(LimitedSubtraction(-69, 69), 0)

    def testcase4(self):
        self.assertEqual(LimitedSubtraction(23, 33), 20)


if __name__ == '__main__':
    unittest.main()