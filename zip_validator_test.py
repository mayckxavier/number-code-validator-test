import unittest
from zip_validator import validate


class ZipValidatorTest(unittest.TestCase):
	
	def test_number_must_be_greater_than_100000(self):
		"""Number must be greater than 100000"""
		
		min_value = validate(100000)
		self.assertEqual(min_value, False)

		min_value = validate(100001)
		self.assertEqual(min_value, True)






if __name__ == '__main__':
	unittest.main()
