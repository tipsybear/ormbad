#!/usr/bin/env python
# setup
# Setup script for ormbad
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Aug 13 12:27:19 2015 -0400
#
# Copyright (C) 2015 Tipsy Bear Studios
# For license information, see LICENSE.txt
#
# ID: setup.py [] benjamin@bengfort.com $

"""
Setup script for ormbad
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

version  = __import__('ormbad').__version__

## Discover the packages
packages = find_packages(where=".", exclude=("tests", "bin", "docs", "fixtures", "register",))

## Load the requirements
requires = []
with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        requires.append(line.strip())

## Define the classifiers
classifiers = (
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: SQL',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Database :: Front-Ends',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
)

## Define the keywords
keywords = ('noorm', 'sql', 'databases', 'postgres')

## Define the description
long_description = ""

## Define the configuration
config = {
    "name": "ormbad",
    "version": version,
    "description": "Why use an ORM when you can just use straight up SQL in Python?",
    "long_description": long_description,
    "license": "Apache 2.0",
    "author": "Benjamin Bengfort",
    "author_email": "benjamin@bengfort.com",
    "url": "https://github.com/tipsybear/ormbad",
    "download_url": 'https://github.com/tipsybear/ormbad/tarball/v%s' % version,
    "packages": packages,
    "install_requires": requires,
    "classifiers": classifiers,
    "keywords": keywords,
    "zip_safe": True,
    "scripts": [],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
