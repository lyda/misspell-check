#!/usr/bin/python

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
    -s     : Create a shell script to interactively correct the file.
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
    p.wait()
    self.assertEquals(p.stderr.read(), '')
    self.assertEquals(len(p.stdout.read().split('\n')), 10)
    self.assertEquals(p.returncode, 0)

  def testBadFile(self):
    p = subprocess.Popen([CLI, 'missing.c'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(p.stderr.read(), '')
    self.assertEquals(len(p.stdout.read().split('\n')), 2)
    self.assertEquals(p.returncode, 0)

  def testGoodFlagF(self):
    p = subprocess.Popen([CLI, '-f', 'good_file_list'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(p.stderr.read(), '')
    self.assertEquals(len(p.stdout.read().split('\n')), 10)
    self.assertEquals(p.returncode, 0)

  def testBadFlagF(self):
    p = subprocess.Popen([CLI, '-f', 'broken_file_list'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(p.stderr.read(), '')
    self.assertEquals(len(p.stdout.read().split('\n')), 2)
    self.assertEquals(p.returncode, 0)

  def testGoodFlagD(self):
    p = subprocess.Popen('( "%s" -d; cat "%s" ) |sort |uniq -u |tail -1' %
                          (CLI, 'example_msl.txt'),
                         cwd=BASE_PATH,
                         shell=True,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(p.stderr.read(), '')
    self.assertEquals(p.stdout.read(), '')
    self.assertEquals(p.returncode, 0)

  def testBadFlagM(self):
    p = subprocess.Popen([CLI, '-d', '-m', 'broken_msl.txt'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertIn('ValueError', p.stderr.read())
    self.assertEquals(p.stdout.read(), '')
    self.assertEquals(p.returncode, 1)

  def testGoodFlagM(self):
    p = subprocess.Popen([CLI, '-d', '-m', 'small_msl.txt'],
                         cwd=BASE_PATH,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(p.stderr.read(), '')
    self.assertEquals(len(p.stdout.read().split('\n')), 3)
    self.assertEquals(p.returncode, 0)

if __name__ == '__main__':
  unittest.main()
