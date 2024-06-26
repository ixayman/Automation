import unittest

import math_function


class TestModuloFunc(unittest.TestCase):
    def test_even_result(self):
        num = 2
        result = math_function.modulo_func(num)
        self.assertEqual(0, result, "wrong result - should be even")

    def test_odd_result(self):
        num = 7
        result = math_function.modulo_func(num)
        self.assertNotEqual(0, result, "wrong result - should be odd")


class TestIsEven(unittest.TestCase):
    def test_true_result(self):
        num = 2
        result = math_function.is_even(num)
        self.assertTrue(result, "wrong result - should be true")

    def test_false_result(self):
        num = 7
        result = math_function.is_even(num)
        self.assertFalse(result, "wrong result - should be false")
