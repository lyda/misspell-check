============
misspellings
============
.. image:: https://secure.travis-ci.org/lyda/misspell-check.png
   :target: https://secure.travis-ci.org/lyda/misspell-check
   :alt: Build status

Spell checker for code
======================
This is a Python library and tool to check for misspelled words in
source code. It does this by looking for words from a list of
common misspellings. The dictionary it uses to do this is based
on the Wikipedia list of common misspellings.

* http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines

The list has been slightly modified to remove some changes that
cause a number of false positives. In particular ``ok->OK`` was
removed (ok is frequently used in perl tests for instance).

Example
=======
To try it out, merely run the following (using an old coreutils
source tree as an example)::

    $ git clone git://git.sv.gnu.org/coreutils -b v8.10 coreutils
    $ find coreutils -name '*.c' | misspellings -f -
    coreutils/src/cat.c:754: efficency -> "efficiency"
    coreutils/src/comm.c:198: funtion -> "function"
    coreutils/src/expr.c:21: seperate -> "separate"
    coreutils/src/pr.c:1417: accomodate -> "accommodate"
    coreutils/src/tac.c:342: unneccessary -> "unnecessary"
    coreutils/src/test.c:91: supressed -> "suppressed"

Contributions
=============
Contributions are welcome! Please add unit tests for new features
or bug fixes. To run all the unit tests run ``./setup.py test``.

Unit tests are run on `Travis`_ for all supported python versions.

TODO
====
Some items on the TODO list:

* Implement option to interactively fix files.
* Give some thought to supporting multiple languages?
* Might a "common misspellings" list be different for different English
  users - might an American make one set of mistakes while a German
  writing English make another? Source of this data?
* Fix pip upgrade bug.

Credits
=======
- `Kevin Lyda`_: Initial shell goo and python version.
- `myint`_: Better python idioms and style. Mixed case support.
- `Maciej Blizinski`_: Potential use in opencsw pushed move to python.
- `Ville Skyttä`_: Sped up wordification, editor-friendly reporting.

.. _`Travis`: http://travis-ci.org/#!/lyda/misspell-check
.. _`Kevin Lyda`: https://github.com/lyda
.. _`myint`: https://github.com/myint
.. _`Maciej Blizinski`: https://github.com/automatthias
.. _`Ville Skyttä`: https://github.com/scop
