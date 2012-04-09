#!/usr/bin/python

import os
import subprocess
import sys
import unittest

BASE_PATH = os.path.dirname(__file__)
LOG_PATH = os.path.join(BASE_PATH, 'logs')
CLI = os.path.join(BASE_PATH, '..', 'misspellings', 'misspellings.py')

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
    p = subprocess.Popen([CLI,
                          os.path.join(BASE_PATH, 'nine_mispellings.c')],
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(len(p.stdout.read().split('\n')), 10)

  def testBadFile(self):
    p = subprocess.Popen([CLI,
                          os.path.join(BASE_PATH, 'missing.c')],
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(len(p.stdout.read().split('\n')), 2)

  def testGoodFlagF(self):
    p = subprocess.Popen([CLI, '-f',
                          os.path.join(BASE_PATH, 'good_file_list')],
                         cwd=BASE_PATH,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(len(p.stdout.read().split('\n')), 10)

  def testBadFlagF(self):
    p = subprocess.Popen([CLI, '-f',
                          os.path.join(BASE_PATH, 'broken_file_list')],
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(len(p.stdout.read().split('\n')), 2)

  def testGoodFlagD(self):
    p = subprocess.Popen('( "%s" -d ; cat "%s" ) | sort | uniq -u' %
                          (CLI, os.path.join(BASE_PATH, 'example_msl.txt')),
                         shell=True,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(p.stdout.read(), '')

  def testBadFlagM(self):
    p = subprocess.Popen([CLI, '-d', '-m',
                          os.path.join(BASE_PATH, 'broken_msl.txt')],
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertIn('ValueError', p.stderr.read())
    self.assertEquals(p.stdout.read(), '')
    self.assertEquals(p.returncode, 1)

  def testGoodFlagM(self):
    p = subprocess.Popen([CLI, '-d', '-m',
                          os.path.join(BASE_PATH, 'small_msl.txt')],
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.wait()
    self.assertEquals(p.stderr.read(), '')
    self.assertEquals(len(p.stdout.read().split('\n')), 3)
    self.assertEquals(p.returncode, 0)

if __name__ == '__main__':
  unittest.main()
