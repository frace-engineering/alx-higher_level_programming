#!/usr/bin/python3
import unittest

class max_integer_test(unittest.TestCase):
    def integer_test(self):
        self.assertAlmostEqual(max_integer([1]), 1)
    
    def type_test(self):
        self.assertRaises(TypeError, maxt_integer, "string")

    def type_test(self):
        self.assertRaises(TypeError, maxt_integer, 'a')

    def type_test(self):
        self.assertRaises(TypeError, maxt_integer, [2 + 1j])
    def max_test(self):
        self.assertAlmostEqual(maxt_integer([2, 4, 9]), 9)
    def max_test(self):
        self.assertAlmostEqual(maxt_integer([2, -19, 9]), 9)
