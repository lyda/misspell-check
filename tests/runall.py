#!/usr/bin/python
"""Run ***ALL*** the testorz!!!"""

import os
import sys
if sys.version_info < (2, 7):
  import unittest2 as unittest
else:
  import unittest

if __name__ == '__main__':
  test_dir = os.path.dirname(globals().get('__file__', os.getcwd()))

  tests = unittest.TestLoader().discover(test_dir)
  runner = unittest.TextTestRunner(verbosity=2)
  result = runner.run(tests)
  if not result.wasSuccessful():
    sys.exit(1)
