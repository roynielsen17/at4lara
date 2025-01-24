#!/usr/bin/env -S python -u
"""
reference other tests in project, or clockworksspheres ramdisk tests
https://github.com/clockworksspheres/ramdisk/tree/master/src/tests
for examples of python tests with the unittest framework
"""

#--- Native python libraries
import sys 
import unittest

sys.path.append("..")

#--- non-native python libraries in this source tree
from tests.lib.genericTestUtilities import GenericTestUtilities


###############################################################################
##### unittest

class test_templates(unittest.TestCase, GenericTestUtilities):
    """
    """

###############################################################################
##### unittest Set Up

    def setUp(self):
        """
        This method runs before each test run.

        """
        unittest.SkipTest("Tests need to be written...")

###############################################################################
##### Method Tests

    ##################################

    def test_at4laraFirstTest(self):
        """
        """
        pass

    ##################################

    def test_at4laraStecondTest(self):
        """
        """
        pass

###############################################################################
##### Functional Tests

    def test_at4laraFirstTest(self):
        """
        """
        pass

    ##################################

    def test_at4laraStecondTest(self):
        """
        """
        pass

###############################################################################
##### unittest Tear Down

    def tearDown(self):
        """
        """
        pass

###############################################################################

if __name__ == "__main__":

    unittest.main()

