#!/usr/bin/env python

import os
import subprocess
import sys
if sys.version_info < (2, 7):
  import unittest2 as unittest
else:
  import unittest

BASE_PATH = os.path.dirname(__file__)
LOG_PATH = os.path.join(BASE_PATH, 'logs')
CLI = os.path.join('..', 'misspellings')


class MisspellingsCLITestCase(unittest.TestCase):
  """
  Test the CLI.

  USAGE: misspellings [-f file] [files]
  Checks files for common spelling mistakes.
    -f file: File containing list of files to check.
    -m file: File containing list of misspelled words & corrections.
    -d     : Dump the list of misspelled words.
    -s file: Create a shell script to interactively correct the file.
    files: Zero or more files to check.
  """

  def setUp(self):
    try:
      os.mkdir(LOG_PATH)
    except:
      pass

  def testGoodFile(self):
    p = subprocess.Popen([CLI, 'nine_mispellings.c'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (output, error_output) = p.communicate()
    self.assertEqual(error_output.decode('utf8'), '')
    self.assertEqual(len(output.decode('utf8').split('\n')), 10)
    self.assertEqual(p.returncode, 0)

  def testBadFile(self):
    p = subprocess.Popen([CLI, 'missing.c'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (output, error_output) = p.communicate()
    self.assertEqual(output.decode('utf8'), '')
    self.assertEqual(len(error_output.decode('utf8').split('\n')), 2)
    self.assertEqual(p.returncode, 0)

  def testGoodFlagF(self):
    p = subprocess.Popen([CLI, '-f', 'good_file_list'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (output, error_output) = p.communicate()
    self.assertEqual(error_output.decode('utf8'), '')
    self.assertEqual(len(output.decode('utf8').split('\n')), 10)
    self.assertEqual(p.returncode, 0)

  def testBadFlagF(self):
    p = subprocess.Popen([CLI, '-f', 'broken_file_list'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (output, error_output) = p.communicate()
    self.assertEqual(output.decode('utf8'), '')
    self.assertEqual(len(error_output.decode('utf8').split('\n')), 2)
    self.assertEqual(p.returncode, 0)

  def testGoodFlagD(self):
    p = subprocess.Popen('( "%s" -d; cat "%s" ) |sort |uniq -u |tail -1' %
                          (CLI, 'example_msl.txt'),
                         cwd=BASE_PATH,
                         shell=True,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (output, error_output) = p.communicate()
    self.assertEqual(error_output.decode('utf8'), '')
    self.assertEqual(output.decode('utf8'), '')
    self.assertEqual(p.returncode, 0)

  def testBadFlagM(self):
    p = subprocess.Popen([CLI, '-d', '-m', 'broken_msl.txt'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (output, error_output) = p.communicate()
    self.assertIn('ValueError', error_output.decode('utf8'))
    self.assertEqual(output.decode('utf8'), '')
    self.assertEqual(p.returncode, 1)

  def testGoodFlagM(self):
    p = subprocess.Popen([CLI, '-d', '-m', 'small_msl.txt'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (output, error_output) = p.communicate()
    self.assertEqual(error_output.decode('utf8'), '')
    self.assertEqual(len(output.decode('utf8').split('\n')), 3)
    self.assertEqual(p.returncode, 0)

  def testBadFlagS(self):
    p = subprocess.Popen([CLI, '-s', 'various_spellings.c'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    (output, error_output) = p.communicate()
    self.assertIn('must not exist', error_output.decode('utf8'))
    self.assertEqual(output.decode('utf8'), '')
    self.assertEqual(p.returncode, 2)

  def testGoodFlagS(self):
    test_out = os.path.join(BASE_PATH, 'various_spellings.test_out')
    good_out = os.path.join(BASE_PATH, 'various_spellings.good_out')
    if os.path.exists(test_out):
      os.unlink(test_out)
    p = subprocess.Popen([CLI, '-s', test_out,
                         'various_spellings.c'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    (output, error_output) = p.communicate(
        input='\n'.encode('utf8'))
    self.assertEqual(error_output.decode('utf8'), '')
    self.assertIn('withdrawl', output.decode('utf8'))
    self.assertEqual(p.returncode, 0)
    self.assertListEqual(open(test_out, 'r').readlines(),
                         open(good_out, 'r').readlines())

  def testStandardIn(self):
    p = subprocess.Popen([CLI, '-f', '-'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    (output, error_output) = p.communicate(
        input='nine_mispellings.c\n'.encode('utf8'))
    self.assertEqual(error_output.decode('utf8'), '')
    self.assertEqual(len(output.decode('utf8').split('\n')), 10)
    self.assertEqual(p.returncode, 0)

if __name__ == '__main__':
  unittest.main()
