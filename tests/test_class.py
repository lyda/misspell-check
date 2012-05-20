#!/usr/bin/env python

import os
import sys
import misspellings_lib as misspellings
if sys.version_info < (2, 7):
  import unittest2 as unittest
else:
  import unittest

BASE_PATH = os.path.dirname(__file__)
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
    misspelling_file = os.path.join(BASE_PATH, 'example_msl.txt')
    ms = misspellings.Misspellings(misspelling_file=misspelling_file)
    lines = 0
    with open(misspelling_file) as msf:
      for unused_line in msf:
        lines += 1
    self.assertEqual(len(ms.dumpMisspellingList()), lines)

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
    self.assertEqual(default_msl, example_msl,
        'See logs in "%s" for dump of the list.' % LOG_PATH)

  def testMissingFile(self):
    ms = misspellings.Misspellings(
        files=os.path.join(BASE_PATH, 'missing_source.c'))
    errors, results = ms.check()
    self.assertEqual(len(errors), 1)

  def testMissingFileWithMultipleFiles(self):
    ms = misspellings.Misspellings(files=[
      os.path.join(BASE_PATH, 'missing_source_%d.c' % i)
      for i in range(10)])
    errors, results = ms.check()
    self.assertEqual(len(errors), 10)
    self.assertEqual(len(results), 0)

  def testGoodFile(self):
    ms = misspellings.Misspellings(files=[
      os.path.join(BASE_PATH, 'nine_mispellings.c')])
    errors, results = ms.check()
    self.assertEqual(len(errors), 0)
    self.assertEqual(len(results), 9)

  def testMoreComplexFile(self):
    ms = misspellings.Misspellings(files=[
      os.path.join(BASE_PATH, 'various_spellings.c')])
    errors, results = ms.check()
    self.assertEqual(len(errors), 0)
    self.assertEqual(len(results), 6)


class UtilityFunctionTestCase(unittest.TestCase):
  def testSameCase(self):
    self.assertEqual('Apple', misspellings.same_case(source='Apple',
                                                     destination='apple'))

    # Do not make lowercase as "Apple" may be the first word in a sentence.
    self.assertEqual('Apple', misspellings.same_case(source='apple',
                                                     destination='Apple'))

  def testSameCaseWithEmptyDestination(self):
    self.assertEqual('', misspellings.same_case(source='apple',
                                                destination=''))
    self.assertEqual('', misspellings.same_case(source='Apple',
                                                destination=''))

  def testSameCaseWithEmptySource(self):
    self.assertEqual('apple', misspellings.same_case(source='',
                                                     destination='apple'))
    self.assertEqual('Apple', misspellings.same_case(source='',
                                                     destination='Apple'))


if __name__ == '__main__':
  unittest.main()
