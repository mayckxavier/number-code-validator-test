import unittest
from zip_validator import validate


class ZipValidatorTest(unittest.TestCase):
    def test_number_must_be_greater_than_minimum(self):
        """Number must be greater than 100000"""

        is_valid = validate(100000)
        self.assertEqual(is_valid, False)

        is_valid = validate(100001)
        self.assertEqual(is_valid, True)

    def test_number_must_be_less_then_max_allowed(self):
        is_valid = validate(999999)
        self.assertEqual(is_valid, False)

        is_valid = validate(9999991)
        self.assertEqual(is_valid, False)

        is_valid = validate(999998)
        self.assertEqual(is_valid, True)


if __name__ == '__main__':
    unittest.main()
