#!/usr/bin/python3
import unittest
from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_init(self):
        data = [2,3]
        result = summation(data)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
