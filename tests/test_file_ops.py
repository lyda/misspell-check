#!/usr/bin/python

import os
import sys
import unittest

# Set the path to load the module being tested.
BASE_PATH = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_PATH, '..'))
import misspellings.misspellings_lib as misspellings


class IntegerArithmenticTestCase(unittest.TestCase):
  def testMissingMSList(self):
    self.assertRaises(IOError, misspellings.Misspellings,
                      None, os.path.join(BASE_PATH, 'missing_msl.txt'))

  def testBrokenMSList(self):
    self.assertRaises(ValueError, misspellings.Misspellings, None,
        os.path.join(BASE_PATH, 'broken_msl.txt'))

  def testMissingFile(self):
    ms = misspellings.Misspellings(
        files=os.path.join(BASE_PATH, 'missing_source.c'))
    errors, results = ms.check()
    self.assertEquals(len(errors), 1)

  def testMissingFiles(self):
    ms = misspellings.Misspellings(files=[
      os.path.join(BASE_PATH, 'missing_source_%d.c' % i)
      for i in xrange(10)])
    errors, results = ms.check()
    self.assertEquals(len(errors), 10)

if __name__ == '__main__':
  unittest.main()
