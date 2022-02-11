import string
import re


def conv_num(num_str):

    # Initialize the helper
    hlp = ConvNumHelper()

    # If the input is not a string type, short circuit the function
    if not isinstance(num_str, str):
        return None

    # Hexadecimal case
    if hlp.is_hex(num_str):
        # If negative
        if hlp.is_negative(num_str):
            return hlp.convert_str_to_hex(num_str[1:]) * -1
        # If positive
        else:
            return hlp.convert_str_to_hex(num_str)

    # Floating point case
    if hlp.is_float(num_str):
        # If negative
        if hlp.is_negative(num_str):
            return hlp.convert_str_to_float(num_str[1:]) * -1
        # If positive
        else:
            return hlp.convert_str_to_float(num_str)

    # Integer case
    if hlp.is_integer(num_str):
        # If negative
        if hlp.is_negative(num_str):
            return hlp.convert_str_to_int(num_str[1:]) * -1
        # If positive
        else:
            return hlp.convert_str_to_int(num_str)

    return None


def my_datetime(num_sec):

    # Initialize a DateTime object
    dt = DateTime(year=1970, month=1, date=1)

    # Get the number of days (using floor)
    days = num_sec // (60 * 60 * 24)

    # While the number of days is greater than zero
    while days > 0:

        # Get the number of days in the current month and year
        days_in_year = dt.days_in_year(dt.year)
        days_in_month = dt.days_in_month(dt.year, dt.month)

        # If the remaining days is greater than those of current year
        if days >= days_in_year:
            dt.increment_year()
            days -= days_in_year

        # if the remaining days is greater than those of the current month
        elif days >= days_in_month:
            dt.increment_month()
            days -= days_in_month

        # Else, increment the date
        else:
            dt.increment_date()
            days -= 1

    return dt.format_as_str()


def hlp_to_byte(num):
    # This function calculate the hexadecimal value for num, and store its
    # bytes in a list
    # Initialize list to store hexadecimal number not in byte format
    not_byte_hex = []
    # Initialize list to store hexadecimal number in byte format
    byte_hex = []
    # List containing all possible digits and letters of a hexadecimal number
    symbols = list("0123456789ABCDEF")

    # Loop to calculate the hexadecimal value for num
    while True:
        if num == 0:
            break
        # Calculate the quotient and remainder of num and 16
        num, rem = divmod(abs(num), 16)
        not_byte_hex.append(symbols[rem])
        # Append 0 at the end of the hexadecimal number if it has an odd
        # number of digits
        if num == 0 and len(not_byte_hex) % 2 != 0:
            not_byte_hex.append("0")

    # Convert the hexadecimal number to byte format and store in a list
    for i in range(len(not_byte_hex[::-1])):
        if i % 2 == 0:
            byte_hex.append(not_byte_hex[::-1][i] + not_byte_hex[::-1][i + 1])
        else:
            continue

    return byte_hex


def hlp_to_str(input_num, input_list):
    # This function convert the list of hexadecimal number's bytes to string
    # and have each byte separated by a space
    output_str = " ".join(input_list)

    # If the input number's value is negative, add negative sign before the
    # hexadecimal number
    if input_num < 0:
        output_str = "-" + output_str

    return output_str


def conv_endian(num, endian='big'):
    # Assume num will always be an integer
    assert isinstance(num, int), "num will always be an integer"

    # Handle the special situation of num=0
    if num == 0:
        return '00'

    # Store the original input number for later use
    input_num = num
    out_list = hlp_to_byte(num)

    # To return a hexadecimal number that is big-endian
    if endian == "big":
        out_str = hlp_to_str(input_num, out_list)
        return out_str

    # To return a hexadecimal number that is little-endian
    elif endian == "little":
        out_str = hlp_to_str(input_num, out_list[::-1])
        return out_str

    # Any other values of endian will return None
    else:
        return None


class ConvNumHelper:
    @staticmethod
    # This function returns the number represented by an ASCII character
    # For example, get_int_from_char('5') returns the int 5
    def get_int_from_char(char):
        # If it is in the 0-9 range
        if char in string.digits:
            return ord(char) - 48
        # If it is a Hex char in the A-F range
        elif char in "ABCDEF":
            return ord(char) - 55
        # If it is a Hex char in the a-f range
        elif char in "abcdef":
            return ord(char) - 87

    # Check if a number string represents an integer like 12345
    def is_integer(self, num_str):

        # If the first character is '-', skip checking it
        string_to_check = num_str
        if self.is_negative(string_to_check):
            string_to_check = num_str[1:]

        for char in string_to_check:
            # Check that each number is within 0-9
            if char not in string.digits:
                return False

        # Check that the length is at least one character or return False
        if len(string_to_check) >= 1:
            return True
        else:
            return False

    # Convert a string that represents an integer into an int
    # For example, convert_str_to_int('12345') returns the int 12345
    def convert_str_to_int(self, num_str):
        # Initialize result to be zero
        result = 0
        # Loop through each character
        for ind in range(0, len(num_str)):
            # Get the number represented by the character
            char = num_str[ind]
            num = self.get_int_from_char(char)
            # Calculate the decimal multiplier using string length and index
            multiplier = pow(10, (len(num_str) - ind - 1))
            # Add to the result
            result += num * multiplier

        return result

    # Check if the first character of the number string is '-'
    # Note that it does not perform other validations on the number string
    @staticmethod
    def is_negative(num_str):

        if len(num_str) < 2:
            return False

        return num_str[0] == '-'

    def is_float(self, num_str):

        # If the first character is '-', skip checking it
        string_to_check = num_str
        if self.is_negative(string_to_check):
            string_to_check = num_str[1:]

        # Initialize decimal point count to be zero
        decimal_pt_count = 0
        for char in string_to_check:
            # Check that each character is within 0-9
            if char in string.digits:
                continue
            # If the character is a decimal point
            elif char == '.':
                # Increment decimal point count
                decimal_pt_count += 1
                # When more than one decimal point has been found
                if decimal_pt_count > 1:
                    return False
            # If the character is neither a digit or a decimal point
            else:
                return False

        # Check that there is exactly one decimal point and at least one digit
        if decimal_pt_count == 1 and len(string_to_check) >= 2:
            return True
        else:
            return False

    def convert_str_to_float(self, num_str):
        # Initialize result to be a float
        result = 0.0

        # Find the decimal point position
        decimal_position = re.search(r'\.', num_str).start()

        # Separate the string into two parts - the whole number and fraction
        whole = num_str[:decimal_position]
        fraction = num_str[decimal_position+1:]

        # Add the whole number part
        result += self.convert_str_to_int(whole)

        # Then add the fraction number part
        for ind in range(0, len(fraction)):
            # Get the number represented by the character
            char = fraction[ind]
            num = self.get_int_from_char(char)

            # Calculate the decimal multiplier using index
            multiplier = pow(10, (ind+1) * -1)

            result += num * multiplier

        return result

    def is_hex(self, num_str):
        # Acceptable characters
        hex_chars = string.digits + 'ABCDEFabcdef'

        string_to_check = num_str
        # If it begins with '-', check the remaining characters
        if self.is_negative(string_to_check):
            string_to_check = string_to_check[1:]

        # Check that the first two characters are '0x'
        if string_to_check[:2] != '0x':
            return False

        # Check the remaining characters after '0x'
        for char in string_to_check[2:]:
            if char not in hex_chars:
                return False

        return True

    def convert_str_to_hex(self, num_str):

        # Initialize result to be 0
        result = 0

        # Loop through each character after 0x
        for ind in range(2, len(num_str)):
            # Get the number represented by the character
            char = num_str[ind]
            num = self.get_int_from_char(char)
            # Calculate the multiplier using string length and index
            multiplier = pow(16, (len(num_str) - ind - 1))
            # Add to the result
            result += num * multiplier

        return result


class DateTime:

    def __init__(self, year=1970, month=1, date=1):
        self.year = year
        self.month = month
        self.date = date

    @staticmethod
    def is_leap_year(year):
        """
        This function test if a given year is a leap year
        :param year: an int that represents a year
        :return: True or False
        """
        # A leap year must be evenly divisible by 4
        if year % 4 == 0:
            # If it is evenly divisible by 400, it is a leap year
            if year % 400 == 0:
                return True
            # If it is divisible by 100 but not 400, it is NOT a leap year
            elif year % 100 == 0:
                return False
            # Otherwise, it is a leap year
            else:
                return True
        # Not evenly divisible by 4, NOT a leap year
        else:
            return False

    def days_in_year(self, year):
        """
        This function returns the number of days in a given year
        :param year: an int that represents a year
        :return: an int that is 365 or 366
        """
        if self.is_leap_year(year):
            return 366
        else:
            return 365

    def days_in_month(self, year, month):
        """
        This function returns the number of days in a given month
        :param year: an int that represents a year
        :param month: an int that represents a month
        :return: an int that represents the number of days in a given month
        """
        long_months = [1, 3, 5, 7, 8, 10, 12]
        short_months = [4, 6, 9, 11]

        # Months that have 31 days
        if month in long_months:
            return 31
        # Months that have 30 days
        elif month in short_months:
            return 30
        # February
        elif month == 2:
            # In a leap year, Feb has 29 days
            if self.is_leap_year(year):
                return 29
            # In a regular year, Feb has 28 days
            else:
                return 28
        else:
            return None

    def get_following_month(self):
        """
        Calling this funtion on a DateTime object returns another DateTime
        object where the year and month represent the month that follows the
        month of the original object.
        :return:
        """
        if self.month == 12:
            return DateTime(year=self.year + 1, month=1)
        else:
            return DateTime(year=self.year, month=self.month + 1)

    def format_as_str(self):
        """
        This function returns a string representation of a DateTime object.
        The format is MM-DD-YYYY
        :return:
        """
        date = self.date if self.date >= 10 else f'0{self.date}'
        month = self.month if self.month >= 10 else f'0{self.month}'
        year = self.year

        return f'{month}-{date}-{year}'

    def increment_year(self, num_years=1):
        self.year += num_years

    def increment_month(self):
        if self.month == 12:
            self.increment_year()
            self.month = 1
        else:
            self.month += 1

    def increment_date(self):
        # If at the end of the month
        if self.date == self.days_in_month(self.year, self.month):
            self.increment_month()
            self.date = 1
        else:
            self.date += 1
