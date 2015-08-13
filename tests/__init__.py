# tests
# Testing for the ormbad module
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Aug 13 12:34:07 2015 -0400
#
# Copyright (C) 2015 Tipsy Bear Studios
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing for the ormbad module
"""

##########################################################################
## Imports
##########################################################################

import unittest

##########################################################################
## Module Constants
##########################################################################

TEST_VERSION = "0.1" ## Also the expected version onf the package

##########################################################################
## Test Cases
##########################################################################

class InitializationTest(unittest.TestCase):

    def test_initialization(self):
        """
        Tests a simple world fact by asserting that 10*10 is 100.
        """
        self.assertEqual(10*10, 100)

    def test_import(self):
        """
        Can import ormbad
        """
        try:
            import ormbad
        except ImportError:
            self.fail("Unable to import the ormbad module!")

    def test_version(self):
        """
        Assert that the version is sane
        """
        import ormbad
        self.assertEqual(TEST_VERSION, ormbad.__version__)
