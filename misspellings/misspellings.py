#!/usr/bin/python

import sys
import getopt
import misspellings_lib as misspellings

def usage(msg=None):
  print 'USAGE: misspellings [-f file] [files]'
  print 'Checks files for common spelling mistakes.'
  print '  -f file: File containing a list of files to check.'
  print '  files: Zero or more files to check.'
  if msg is not None:
    print 'ERROR: %s' % msg
    sys.exit(1)
  sys.exit(0)


if __name__ == '__main__':
  try:
    flags, files = getopt.getopt(sys.argv[1:], 'f:vh')
  except getopt.GetoptError, e:
    usage(e)
  for flag, option in flags:
    if flag == '-f':
      if option == '-':
        f = sys.stdin
      else:
        try:
          f = open(option, 'r')
        except IOError, e:
          usage(e)
      for line in f:
        files.append(line.strip())
    elif flag == '-v':
      print 'Version 1.0'
      sys.exit(0)
    elif flag == '-h':
      usage()
  ms = misspellings.Misspellings(files=files)
  errors, results = ms.check()
  for res in results:
    print '%s[%d]: %s -> %s' % (res[0], res[1], res[2], ','.join(
      ['"%s"' % w for w in ms.suggestions(res[2])]))
  for err in errors:
    print 'ERROR: %s' % err
