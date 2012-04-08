#!/usr/bin/python
"""Run ***ALL*** the testorz!!!"""

import unittest
import imp
import glob
import os

cwd = os.path.dirname(globals().get('__file__', os.getcwd()))

test_list = [(os.path.basename(f)[:-3], f)
             for f in glob.glob(os.path.join(cwd, 'test_*.py'))]
for test_module, test_file in test_list:
  test_runner = imp.load_source(test_module, test_file)
  print 'Running test suit "%s"' % test_module
  suite = unittest.defaultTestLoader.loadTestsFromModule(test_runner)
  unittest.TextTestRunner(verbosity=2).run(suite)
