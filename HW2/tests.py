"""
CS362 HW2: Improving Coverage
Author: Xiaoying Li
"""


import unittest
from contrived_func import contrived_func


class TestBranchAndConditionCoverage(unittest.TestCase):
    # C2, C4, C7
    def test1(self):
        self.assertFalse(contrived_func(6))

    # C2, C4, C8
    def test2(self):
        self.assertTrue(contrived_func(47))

    # C2, C5, C12
    def test3(self):
        self.assertFalse(contrived_func(49))

    # C2, C6, C11
    def test4(self):
        self.assertTrue(contrived_func(75))

    # C2, C9
    def test5(self):
        self.assertTrue(contrived_func(80))

    # C1
    def test6(self):
        self.assertTrue(contrived_func(101))

    # C3, C6, C10
    def test7(self):
        self.assertFalse(contrived_func(151))


if __name__ == '__main__':
    unittest.main()
