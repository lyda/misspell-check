============
misspellings
============
.. image:: https://secure.travis-ci.org/myint/misspell-check.png
   :target: https://secure.travis-ci.org/myint/misspell-check
   :alt: Build status


This is a Python library and tool to check for misspelled
words in source code.  It does this by looking for words from
a list of common misspellings.  The dictionary it uses to do this
is based on the Wikipedia list of common misspellings.

* http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines

The list has been slightly modified to remove some changes that cause
a number of false positives.  In particular `ok->OK` was removed (ok is
frequently used in perl tests for instance).

To try it out, merely run the following (using the coreutils
source tree as an example)::

    $ git clone git://git.sv.gnu.org/coreutils ../coreutils
    $ find ../coreutils -name '*.c' | misspellings -f -
    ../coreutils/src/cat.c[754]: efficency -> "efficiency"
    ../coreutils/src/comm.c[196]: funtion -> "function"
    ../coreutils/src/expr.c[21]: seperate -> "separate"
    ../coreutils/src/pr.c[1416]: accomodate -> "accommodate"
    ../coreutils/src/tac.c[342]: unneccessary -> "unnecessary"
    ../coreutils/src/test.c[97]: supressed -> "suppressed"

CREDITS
=======

- `Kevin Lyda`_: initial shell goo and python version.
- `myint`_: Support for python 3 and some initial support for utf8.
- `Maciej Blizinski`_: potential use in opencsw pushed move to python.

.. _`Kevin Lyda`: https://github.com/lyda
.. _`myint`: https://github.com/myint
.. _`Maciej Blizinski`: https://github.com/automatthias
