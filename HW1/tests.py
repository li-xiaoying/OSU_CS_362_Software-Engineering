"""
CS362 HW1: Writing Black Box Tests
Author: Xiaoying Li
Test Generation Methodology: All test cases are generated manually using error
                             guessing and boundary values checking method.
"""


import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    # Verifies if empty credit card number returns False.
    # Generated manually using common error guessing, if the function handled
    # string with size=0 properly.
    # Bug 1 found.
    def test_empty(self):
        credit_card_number = ""
        message = "Empty number"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if Visa credit card number with valid prefix and check digit,
    # but too short length (length<16) returns False.
    # Generated manually using boundary values checking, length of Visa credit
    # card number should be 16, checking if the function handled string with
    # too small size=15 properly.
    # Bug 2 found.
    def test_visa_length_too_short(self):
        credit_card_number = "400000000000006"
        message = "Visa: too short"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if MasterCard credit card number with valid prefix and check
    # digit, but too short length (length<16) returns False.
    # Generated manually using boundary values checking, length of MaterCard
    # credit card number should be 16, checking if the function handled string
    # with too small size=15 properly.
    def test_mastercard_length_too_short(self):
        credit_card_number = "510000000000003"
        message = "MasterCard: too short"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if American Express credit card number with valid prefix and
    # check digit, but too short length (length<15) returns False.
    # Generated manually using boundary values checking, length of American
    # Express credit card number should be 16, checking if the function
    # handled string with too small size=14 properly.
    def test_american_express_length_too_short(self):
        credit_card_number = "34000000000000"
        message = "American Express: too short"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if Visa credit card number with valid prefix and check digit,
    # but too long length (length>16) returns False.
    # Generated manually using boundary values checking, length of Visa credit
    # card number should be 16, checking if the function handled string with
    # too big size=17 properly.
    def test_visa_length_too_long(self):
        credit_card_number = "40000000000000006"
        message = "Visa: too long"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if MasterCard credit card number with valid prefix and check
    # digit, but too long length (length>16) returns False.
    # Generated manually using boundary values checking, length of MaterCard
    # credit card number should be 16, checking if the function handled string
    # with too large size=17 properly.
    def test_mastercard_length_too_long(self):
        credit_card_number = "55000000000000002"
        message = "MasterCard: too long"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if American Express credit card number with valid prefix and
    # check digit, but too long length (length>15) returns False.
    # Generated manually using boundary values checking, length of American
    # Express credit card number should be 15, checking if the function
    # handled string with too large size=16 properly.
    # Bug 5 found.
    def test_american_express_length_too_long(self):
        credit_card_number = "3400000000000000"
        message = "American Express: too long"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if Visa credit card number with valid prefix and length, but
    # invalid check digit returns False.
    # Generated manually using common error guessing, if the function handled
    # invalid check digit properly.
    def test_visa_bad_check_digit(self):
        credit_card_number = "4000000000000001"
        message = "Visa: bad check digit"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if MasterCard credit card number with valid prefix and length,
    # but invalid check digit returns False.
    # Generated manually using common error guessing, if the function handled
    # invalid check digit properly.
    def test_mastercard_bad_check_digit(self):
        credit_card_number = "2221000000000001"
        message = "MasterCard: bad check digit"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if American Express credit card number with valid prefix and
    # length, but invalid check digit returns False.
    # Generated manually using common error guessing, if the function handled
    # invalid check digit properly.
    # Bug 4 found.
    def test_american_express_bad_check_digit(self):
        credit_card_number = "340000000000001"
        message = "American Express: bad check digit"
        self.assertFalse(credit_card_validator(credit_card_number), message)

    # Verifies if valid Visa credit card number returns True.
    # Generated manually using common error guessing, if the function handled
    # valid credit card number properly.
    def test_valid_visa(self):
        credit_card_number = "4000000000000002"
        message = "Valid Visa number"
        self.assertTrue(credit_card_validator(credit_card_number), message)

    # Verifies if valid MasterCard credit card number returns True.
    # Generated manually using common error guessing, if the function handled
    # valid credit card number properly.
    # Bug 6 found.
    def test_valid_mastercard(self):
        credit_card_number = "2720000000000005"
        message = "Valid MasterCard number"
        self.assertTrue(credit_card_validator(credit_card_number), message)

    # Verifies if valid American Express credit card number returns True.
    # Generated manually using common error guessing, if the function handled
    # valid credit card number properly.
    def test_valid_american_express(self):
        credit_card_number = "370000000000002"
        message = "Valid American Express number"
        self.assertTrue(credit_card_validator(credit_card_number), message)

    # Verifies if valid credit card number entered as an integer not string
    # returns False.
    # Generated manually using common error guessing, if the function handled
    # invalid data type properly.
    # Bug 3 found.
    def test_not_string(self):
        credit_card_number = 4000000000000002
        message = "Valid but not string number"
        self.assertFalse(credit_card_validator(credit_card_number), message)


if __name__ == '__main__':
    unittest.main()
