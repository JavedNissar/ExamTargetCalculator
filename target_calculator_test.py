import unittest
import target_calculator as tc

class target_calculator_test(unittest.TestCase):
    simpleCase = [1,2,3]
    simpleCoefficients = [1,1,1]
    def test_sum_of_products_mutability(self):
        tc.calculate_sum_of_products(self.simpleCase, self.simpleCoefficients)

        self.assertEqual(self.simpleCase, [1,2,3])

        self.assertEqual(self.simpleCoefficients, [1,1,1])

    def test_sum_of_products_simple(self):
        result = tc.calculate_sum_of_products(self.simpleCase, \
                self.simpleCoefficients)

        expected = 6

        self.assertEqual(expected, result)

    def test_sum_of_products_interesting(self):
        result = tc.calculate_sum_of_products(self.simpleCase,[0.1,0.4,0.5])

        expected = 2.4

        self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main(exit=False)
