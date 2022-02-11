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
