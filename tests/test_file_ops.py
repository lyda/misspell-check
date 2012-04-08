#!/usr/bin/python

import os
import sys
import unittest

# Set the path to load the module being tested.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
print sys.path
import misspellings.misspellings_lib as misspellings


class IntegerArithmenticTestCase(unittest.TestCase):
  def testAdd(self):  ## test method names begin 'test*'
    self.assertEqual((1 + 2), 3)
    self.assertEqual(0 + 1, 1)
  def testMultiply(self):
    self.assertEqual((0 * 10), 0)
    self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
  unittest.main()
