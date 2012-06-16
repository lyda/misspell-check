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
If you have `tox`_ installed, just run ``tox``.

You can review `coverage`_ of added tests by running
``coverage run setup.py test`` and then running
``coverage report -m``.

Note that tests are run on `Travis`_ for all supported python
versions whenever the tree on github is pushed to.

TODO
====
Some items on the TODO list:

* Implement option to interactively fix files.
* Give some thought to supporting multiple languages?
* Might a "common misspellings" list be different for different English
  users - might an American make one set of mistakes while a German
  writing English make another? Source of this data?
* Fix sed flag.  Have it support sed -i optionally, have it output all
  unambiguous sed commands, have it be more careful on what it
  replaces. It might also be an idea to have a perl output option.
* Use generators to allow finding errors as you go. Currently misspellings
  grabs all files first, then checks them, which can take a while.

Credits
=======
- `Kevin Lyda`_: Initial shell goo and python version.
- `myint`_: Better python idioms and style. Mixed case support.
  Travis/tox support.
- `Maciej Blizinski`_: Potential use in opencsw pushed move to python.
- `Ville Skyttä`_: Sped up wordification, editor-friendly reporting.

.. _`tox`: http://pypi.python.org/pypi/tox
.. _`coverage`: http://pypi.python.org/pypi/coverage
.. _`Travis`: http://travis-ci.org/#!/lyda/misspell-check
.. _`Kevin Lyda`: https://github.com/lyda
.. _`myint`: https://github.com/myint
.. _`Maciej Blizinski`: https://github.com/automatthias
.. _`Ville Skyttä`: https://github.com/scop
