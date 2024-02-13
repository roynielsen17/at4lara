#!/usr/bin/env -S python -u
"""
Test for basic functionality of the RisDataModel
"""
import os
import sys
import unittest

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)

# --- Non-native python libraries in this source tree
from at4lara.RisDataModel import RisDataModel
from at4lara.RisDataModel import refTypes
from at4lara.RisDataModel import refTags
 

class test_RisDataModel(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        """
        self.rTy = refTypes
        self.rTa = refTags
        self.rdm = RisDataModel()

    def test_getters_01(self):
        """
        make sure all of the tags have a getter
        """
        for key in refTags.keys():
            self.assertTrue("get" + key in dir(self.rdm), "key " + str(key) + " Not In RisDataModel")

    def test_getters_02(self):
        """
        make sure there are no more getters than there are in the tag list
        """
        for item in dir(self.rdm) 
        keylen = self.rTa.keys().len()
        self.assertTrue(mods == keylen, "getters don't equal the number of tags...")

    # ---------------

    def test_setters_01(self):
        """
        make sure all of the tags have a setter
        """
        for key in refTags.keys():
            self.assertTrue("set" + key in dir(self.rdm), "key " + str(key) + " Not In RisDataModel")

    def test_setters_02(self):
        """
        make sure there are no more setters than there are in the tag list
        """
        pass

    # ---------------
 
    def test_refTagGetterSetterMatches_01(self):
        """
        make sure that every getter has a setter match.
        """
        pass
 
###############################################################################


if __name__ == "__main__":
    unittest.main()




