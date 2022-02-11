import unittest
from check_pwd import check_pwd


class TestCheckPwd(unittest.TestCase):
    def test_empty_string(self):
        pwd = ""
        self.assertFalse(check_pwd(pwd))

    def test_nonempty_valid_string(self):
        pwd = "CS_372-a2"
        self.assertTrue(check_pwd(pwd))

    def test_too_short_string(self):
        pwd = "CS_372a"
        self.assertFalse(check_pwd(pwd))

    def test_too_long_string(self):
        pwd = "CS_372-a2~tdd~hands~on"
        self.assertFalse(check_pwd(pwd))

    def test_no_lowercase_string(self):
        pwd = "CS_372-A2"
        self.assertFalse(check_pwd(pwd))

    def test_no_uppercase_string(self):
        pwd = "cs_372-a2"
        self.assertFalse(check_pwd(pwd))

    def test_no_digit_string(self):
        pwd = "TDD_hands_on"
        self.assertFalse(check_pwd(pwd))

    def test_no_symbol_string(self):
        pwd = "CS372a2tdd"
        self.assertFalse(check_pwd(pwd))

    def test_not_permitted_symbol_string(self):
        pwd = "CS_372-a2{"
        self.assertFalse(check_pwd(pwd))


if __name__ == '__main__':
    unittest.main()
