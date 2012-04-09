#!/usr/bin/env python
from setuptools import setup

requires = []

try:
    import re
except ImportError:
    requires.append('re')

entry_points = {
}

setup(
    name = "misspellings",
    version = "1.0",
    url = 'http://github.org/lyda/misspell-check',
    author = 'Kevin Lyda',
    author_email = 'kevin@ie.suberic.net',
    description = "A tool to detect misspellings",
    long_description=open('README.md').read(),
    packages = ['misspellings', ],
    scripts = ['scripts/misspellings', ],
    install_requires = requires,
    test_suite = 'tests.runall',
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities',
                   ],
)
