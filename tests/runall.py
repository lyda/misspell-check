#!/usr/bin/python
"""Run ***ALL*** the testorz!!!"""

import glob
import os
import sys
import unittest

cwd = os.path.dirname(globals().get('__file__', os.getcwd()))

tests = unittest.TestLoader().discover(cwd)
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(tests)
if not result.wasSuccessful():
  sys.exit(1)
