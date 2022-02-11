import unittest
from task import conv_num
from task import DateTime
from task import my_datetime
from task import conv_endian


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


class TestDateTime(unittest.TestCase):

    def test_leap_year_1972(self):
        dt = DateTime()
        self.assertTrue(dt.is_leap_year(1972))

    def test_leap_year_1900(self):
        dt = DateTime()
        self.assertFalse(dt.is_leap_year(1900))

    def test_leap_year_2400(self):
        dt = DateTime()
        self.assertTrue(dt.is_leap_year(2400))

    def test_days_in_month_jan_2000(self):
        dt = DateTime()
        self.assertEqual(dt.days_in_month(2000, 1), 31)

    def test_days_in_month_feb_2000(self):
        dt = DateTime()
        self.assertEqual(dt.days_in_month(2000, 2), 29)

    def test_days_in_month_sep_1972(self):
        dt = DateTime()
        self.assertEqual(dt.days_in_month(1972, 9), 30)

    def test_days_in_month_feb_2021(self):
        dt = DateTime()
        self.assertEqual(dt.days_in_month(2021, 2), 28)

    def test_days_in_year_1972(self):
        dt = DateTime()
        self.assertEqual(dt.days_in_year(1972), 366)

    def test_days_in_year_1900(self):
        dt = DateTime()
        self.assertEqual(dt.days_in_year(1900), 365)

    def test_days_in_year_2400(self):
        dt = DateTime()
        self.assertEqual(dt.days_in_year(2400), 366)

    def test_format_as_str(self):
        dt = DateTime(year=1999, month=1, date=1)
        self.assertEqual(dt.format_as_str(), '01-01-1999')


class TestMyDateTime(unittest.TestCase):

    def test_0(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test_1(self):
        self.assertEqual(my_datetime(1), "01-01-1970")

    def test_one_day(self):
        self.assertEqual(my_datetime(60 * 60 * 24), "01-02-1970")

    def test_one_month(self):
        self.assertEqual(my_datetime(60 * 60 * 24 * 31), "02-01-1970")

    def test_one_year(self):
        self.assertEqual(my_datetime(60 * 60 * 24 * 365), "01-01-1971")

    def test_one_year_one_month_one_day(self):
        num_secs = 60 * 60 * 24 * (365 + 31 + 1)
        self.assertEqual(my_datetime(num_secs), "02-02-1971")

    def test_one_year_one_month_one_day_one_hour(self):
        num_secs = 60 * 60 * 24 * (365 + 31 + 1) + 60 * 60
        self.assertEqual(my_datetime(num_secs), "02-02-1971")

    def test_123456789(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test_9876543210(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    def test_201653971200(self):
        self.assertEqual(my_datetime(201653971200), "02-29-8360")


class TestConvEndian(unittest.TestCase):
    def test_positive_big(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_positive(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_negative(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_positive_little(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_negative_little(self):
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_format(self):
        self.assertEqual(conv_endian(num=-954786, endian='little'),
                         '-A2 91 0E')

    def test_wrong_endian1(self):
        self.assertIsNone(conv_endian(num=-954786, endian='small'))

    def test_wrong_endian2(self):
        self.assertIsNone(conv_endian(954786, 'large'))

    def test_zero(self):
        self.assertEqual(conv_endian(0, 'little'), '00')

    def test_negative_zero(self):
        self.assertEqual(conv_endian(-0, 'little'), '00')

    def test_positive_single_digit(self):
        self.assertEqual(conv_endian(15, 'little'), '0F')

    def test_negative_single_digit(self):
        self.assertEqual(conv_endian(-15, 'big'), '-0F')

    def test_positive_double_digits(self):
        self.assertEqual(conv_endian(17, 'big'), '11')

    def test_negative_double_digits(self):
        self.assertEqual(conv_endian(-17, 'little'), '-11')


if __name__ == '__main__':
    unittest.main()
