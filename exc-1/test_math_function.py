import unittest

import math_function


class TestModuloFunc(unittest.TestCase):
    def test_modulo_func_even_result(self):
        num = 2
        result = math_function.modulo_func(num)
        self.assertEqual(0, result, "wrong result - should be even")

    def test_modulo_func_odd_result(self):
        num = 7
        result = math_function.modulo_func(num)
        self.assertNotEqual(0, result, "wrong result - should be odd")

    def test_is_even_true_result(self):
        num = 2
        result = math_function.is_even(num)
        self.assertTrue(result, "wrong result - should be true")

    def test_is_even_false_result(self):
        num = 1
        result = math_function.is_even(num)
        self.assertFalse(result, "wrong result - should be false")

    def test_is_odd_true_result(self):
        num = 1
        result = math_function.is_odd(num)
        self.assertTrue(result, "wrong result - should be true")

    def test_is_odd_false_result(self):
        num = 2
        result = math_function.is_odd(num)
        self.assertFalse(result, "wrong result - should be false")

    def test_sum_function_positive_numbers(self):
        num_a = 1
        num_b = 2
        summ = 3
        result = math_function.sum_function(num_a, num_b)
        self.assertEqual(summ, result, "positive numbers - wrong sum")

    def test_sum_function_negative_numbers(self):
        num_a = -1
        num_b = -2
        summ = -3
        result = math_function.sum_function(num_a, num_b)
        self.assertEqual(summ, result, "negative numbers - wrong sum")

    def test_sum_function_positive_and_negative(self):
        num_a = [1, -1]
        num_b = [-2, 2]
        summ = [-1, 1]
        for i in range(len(num_a)):
            result = math_function.sum_function(num_a[i], num_b[i])
            self.assertEqual(summ[i], result, "negative & positive numbers - wrong sum")

    def test_sum_function_with_zero(self):
        num_a = [0, 0, 1, -1, 0]
        num_b = [0, 1, 0, 0, -1]
        summ = [0, 1, 1, -1, -1]
        for i in range(len(num_a)):
            result = math_function.sum_function(num_a[i], num_b[i])
            self.assertEqual(summ[i], result, "sum with zero - wrong sum")

    def test_sum_function_large_numbers(self):
        num_a = 1000000
        num_b = 2000000
        summ = 3000000
        result = math_function.sum_function(num_a, num_b)
        self.assertEqual(summ, result, "sub large numbers - wrong sum")

    def test_sub_function_positive_numbers(self):
        num_a = 2
        num_b = 1
        subb = 1
        result = math_function.sub_function(num_a, num_b)
        self.assertEqual(subb, result, "positive numbers - wrong sub result")

    def test_sub_function_negative_numbers(self):
        num_a = -1
        num_b = -2
        subb = 1
        result = math_function.sub_function(num_a, num_b)
        self.assertEqual(subb, result, "negative numbers - wrong sub result")

    def test_sub_function_positive_and_negative(self):
        num_a = [1, -1]
        num_b = [-2, 2]
        subb = [3, -3]
        for i in range(len(num_a)):
            result = math_function.sub_function(num_a[i], num_b[i])
            self.assertEqual(subb[i], result, "negative & positive numbers - wrong sub result")

    def test_sub_function_with_zero(self):
        num_a = [0, 0, 1, -1, 0]
        num_b = [0, 1, 0, 0, -1]
        subb = [0, -1, 1, -1, 1]
        for i in range(len(num_a)):
            result = math_function.sub_function(num_a[i], num_b[i])
            self.assertEqual(subb[i], result, "sub with zero - wrong sub result")

    def test_sub_function_large_numbers(self):
        num_a = 2000000
        num_b = 1000000
        subb = 1000000
        result = math_function.sub_function(num_a, num_b)
        self.assertEqual(subb, result, "sub large numbers - wrong sub result")
