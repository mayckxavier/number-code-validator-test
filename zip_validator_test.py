import unittest
from zip_validator import validate


class ZipValidatorTest(unittest.TestCase):
    def test_must_be_a_valid_number(self):
        """Number must be a valid value"""

        is_valid = validate(100110)
        self.assertEqual(is_valid, True)

        is_valid = validate(990099)
        self.assertEqual(is_valid, True)

    def test_must_be_an_invalid_number(self):
        """Number must be an invalid value"""

        is_valid = validate('jose')
        self.assertEqual(is_valid, False)

        is_valid = validate(1000001)
        self.assertEqual(is_valid, False)

        is_valid = validate(9999991)
        self.assertEqual(is_valid, False)

        is_valid = validate(100)
        self.assertEqual(is_valid, False)

    def test_number_must_be_greater_than_minimum(self):
        """Number must be greater than 100000"""

        is_valid = validate(100000)
        self.assertEqual(is_valid, False)

        is_valid = validate(100110)
        self.assertEqual(is_valid, True)

    def test_number_must_be_less_then_max_allowed(self):
        is_valid = validate(999999)
        self.assertEqual(is_valid, False)

        is_valid = validate(9999991)
        self.assertEqual(is_valid, False)

        is_valid = validate(990099)
        self.assertEqual(is_valid, True)

    def test_if_number_has_duplicate_digits(self):
        """
            Number can't have duplicate alternate digits
            121426 # Invalid 
            523563 # Valid 
            552523 # Invalid 
            112233 # Valid
        """
        is_valid = validate(121426)
        self.assertEqual(is_valid, False)

        is_valid = validate(523563)
        self.assertEqual(is_valid, True)

        is_valid = validate(552523)
        self.assertEqual(is_valid, False)

        is_valid = validate(112233)
        self.assertEqual(is_valid, True)


if __name__ == '__main__':
    unittest.main()
