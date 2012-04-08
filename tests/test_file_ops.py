#!/usr/bin/python

import os
import sys
import unittest

# Set the path to load the module being tested.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import misspellings.misspellings_lib as misspellings


class IntegerArithmenticTestCase(unittest.TestCase):
  def testMissingList(self):
    self.assertRaises(IOError, misspellings.Misspellings,
                      None, 'missing_msl.txt')
  def testMultiply(self):
    self.assertEqual((0 * 10), 0)
    self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
  unittest.main()
