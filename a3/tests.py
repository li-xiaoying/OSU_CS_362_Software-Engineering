import unittest
from task import conv_num


class TestConvNum(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(conv_num('12345'), 12345)

    def test_integer_with_leading_zero(self):
        self.assertEqual(conv_num('012345'), 12345)

    def test_negative_integer(self):
        self.assertEqual(conv_num('-12345'), -12345)

    def test_positive_float(self):
        self.assertEqual(conv_num('123.45'), 123.45)

    def test_negative_float(self):
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test_float_with_leading_decimal_point(self):
        self.assertEqual(conv_num('.45'), 0.45)

    def test_float_with_trailing_decimal_point(self):
        self.assertEqual(conv_num('123.'), 123.0)

    def test_positive_hex_num(self):
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test_negative_hex_num(self):
        self.assertEqual(conv_num('-0xFF'), -255)

    def test_invalid_hex_num(self):
        self.assertIsNone(conv_num('0xAZ4'))

    def test_positive_hex_lower(self):
        self.assertEqual(conv_num('0xad4'), 2772)

    def test_int_with_trailing_letter(self):
        self.assertIsNone(conv_num('12345A'))

    def test_float_with_double_decimal_points(self):
        self.assertIsNone(conv_num('12.3.45'))

    def test_non_string_input(self):
        self.assertIsNone(conv_num(12345))

    def test_empty_string(self):
        self.assertIsNone(conv_num(''))

    def test_minus_sign(self):
        self.assertIsNone(conv_num('-'))

    def test_decimal_point(self):
        self.assertIsNone(conv_num('.'))


if __name__ == '__main__':
    unittest.main()
