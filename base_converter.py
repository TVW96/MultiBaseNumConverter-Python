import unittest

# Import the conversion function from your base converter module
from MultiBaseNumConverter import convert_number

class TestBaseConverter(unittest.TestCase):

    # Test binary to decimal
    def test_binary_to_decimal(self):
        self.assertEqual(convert_number('1010', 2, 10), '10')
        self.assertEqual(convert_number('1111', 2, 10), '15')

    # Test decimal to binary
    def test_decimal_to_binary(self):
        self.assertEqual(convert_number('10', 10, 2), '1010')
        self.assertEqual(convert_number('15', 10, 2), '1111')

    # Test hexadecimal to decimal
    def test_hexadecimal_to_decimal(self):
        self.assertEqual(convert_number('1A', 16, 10), '26')
        self.assertEqual(convert_number('FF', 16, 10), '255')

    # Test decimal to hexadecimal
    def test_decimal_to_hexadecimal(self):
        self.assertEqual(convert_number('255', 10, 16), 'FF')
        self.assertEqual(convert_number('26', 10, 16), '1A')

    # Test octal to decimal
    def test_octal_to_decimal(self):
        self.assertEqual(convert_number('12', 8, 10), '10')
        self.assertEqual(convert_number('17', 8, 10), '15')

    # Test decimal to octal
    def test_decimal_to_octal(self):
        self.assertEqual(convert_number('10', 10, 8), '12')
        self.assertEqual(convert_number('15', 10, 8), '17')

    # Test base 16 to base 2 (hexadecimal to binary)
    def test_hex_to_binary(self):
        self.assertEqual(convert_number('1A', 16, 2), '11010')
        self.assertEqual(convert_number('FF', 16, 2), '11111111')

    # Test base 2 to base 16 (binary to hexadecimal)
    def test_binary_to_hex(self):
        self.assertEqual(convert_number('11111111', 2, 16), 'FF')
        self.assertEqual(convert_number('11010', 2, 16), '1A')

    # Test base 10 to base 10 (no conversion needed)
    def test_base_10_to_base_10(self):
        self.assertEqual(convert_number('1234', 10, 10), '1234')

    # Test edge case with zero
    def test_zero(self):
        self.assertEqual(convert_number('0', 10, 2), '0')
        self.assertEqual(convert_number('0', 2, 16), '0')
        self.assertEqual(convert_number('0', 16, 10), '0')


# This block will automatically run the test when executed directly
if __name__ == '__main__':
    unittest.main()
