============
misspellings
============

-------------------------------------
misspellings - spell checker for code
-------------------------------------

:Author:         Kevin Lyda <kevin@ie.suberic.net>
:Manual section: 1
:Manual group:   Utilities


Synopsis
--------
**misspellings** misspellings [*options*] [*files*]

Usage: misspellings [-f file_list] [files]

Checks files for common spelling mistakes.

Options:
  -v, --version  Show the version number and exit.
  -h, --help     Show this help message and exit.
  -f file        File containing list of files to check.
  -m file        File containing list of misspelled words & corrections.
  -d             Dump the list of misspelled words.
  -i             Interactively fix the file.
  -s file        Create a shell script to interactively correct the files -
                 script saved to the given file.

  files: Zero or more files to check.

Description
-----------
The **misspellings** command provides a command line tool to spell
check code.

For basic usage, run with a list of files or use the ``-f`` option
to specify a list of files to check. Use ``-f -`` to read a list
of files from stdin.

To simplify modifying code, use the ``-s`` flag to generate a sed
script to change the code. Make sure the check the results, perhaps
using ``diff``.

Currently the tool only checks for common misspellings in English.
If you can come up with a list for a different language, use the
``-m`` option.

Bugs
----
Quite possibly. Report them via the issue tracker at the project
website:

https://github.com/lyda/misspell-check/issues


See Also
--------
http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings

Resources
---------
Project website: http://github.com/lyda/misspell-check

Copying
-------
Copyright (C) 2012 Kevin Lyda.
Free use of this software is granted under the terms of the Apache
License.
