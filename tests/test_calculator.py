import unittest
from src.calculator import add, divide


class TestCalculator(unittest.TestCase):
    """Unit tests for the calculator module functions."""

    def test_add_integers(self):
        """Test adding two positive integers."""
        self.assertEqual(add(2, 3), 5)

    def test_add_floats(self):
        """Test adding floating-point numbers."""
        self.assertAlmostEqual(add(5.5, 4.5), 10.0)

    def test_add_negative_numbers(self):
        """Test adding negative numbers together."""
        self.assertEqual(add(-1, -1), -2)

    def test_divide_valid(self):
        """Test normal, valid division operations."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero_raises_value_error(self):
        """Test that dividing by zero correctly raises a ValueError exception."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)

        # Verify the custom error message matches what you wrote in the function
        self.assertEqual(str(context.exception), "The divisor cannot be zero.")


if __name__ == '__main__':
    unittest.main()
