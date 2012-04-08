#!/usr/bin/python

import os
import sys
import unittest

# Set the path to load the module being tested.
BASE_PATH = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_PATH, '..'))
import misspellings.misspellings_lib as misspellings


LOG_PATH = os.path.join(BASE_PATH, 'logs')

class MisspellingsTestCase(unittest.TestCase):
  def setUp(self):
    try:
      os.mkdir(LOG_PATH)
    except:
      pass

  def testMissingMSList(self):
    self.assertRaises(IOError, misspellings.Misspellings,
                      None, os.path.join(BASE_PATH, 'missing_msl.txt'))

  def testBrokenMSList(self):
    self.assertRaises(ValueError, misspellings.Misspellings, None,
        os.path.join(BASE_PATH, 'broken_msl.txt'))

  def testGoodMSList(self):
    ms = misspellings.Misspellings(
        misspelling_file=os.path.join(BASE_PATH, 'example_msl.txt'))
    # wc -l example_msl.txt
    self.assertEquals(len(ms.dumpMisspellingList()), 4462)

  def testExampleSameAsDefault(self):
    dms = misspellings.Misspellings()
    ems = misspellings.Misspellings(
        misspelling_file=os.path.join(BASE_PATH, 'example_msl.txt'))
    # wc -l example_msl.txt
    default_msl = dms.dumpMisspellingList()
    example_msl = ems.dumpMisspellingList()
    for fn, msl in (('msl_ex', example_msl), ('msl_de', default_msl)):
      f = open(os.path.join(LOG_PATH,
                            'testExampleSameAsDefault.%s.tmp' % fn), 'w')
      for w, c in msl:
        f.write('%s %s\n' % (w, c))
      f.close()
    self.assertEquals(default_msl, example_msl,
        'See logs in "%s" for dump of the list.' % LOG_PATH)

  def testMissingFile(self):
    ms = misspellings.Misspellings(
        files=os.path.join(BASE_PATH, 'missing_source.c'))
    errors, results = ms.check()
    self.assertEquals(len(errors), 1)

  def testMissingFile(self):
    ms = misspellings.Misspellings(files=[
      os.path.join(BASE_PATH, 'missing_source_%d.c' % i)
      for i in xrange(10)])
    errors, results = ms.check()
    self.assertEquals(len(errors), 10)
    self.assertEquals(len(results), 0)

  def testGoodFile(self):
    ms = misspellings.Misspellings(files=[
      os.path.join(BASE_PATH, 'nine_mispellings.c')])
    errors, results = ms.check()
    self.assertEquals(len(errors), 0)
    self.assertEquals(len(results), 9)

if __name__ == '__main__':
  unittest.main()
