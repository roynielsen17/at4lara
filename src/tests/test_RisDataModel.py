#!/usr/bin/env -S python -u
"""
Test for basic functionality of the RisDataModel
"""
import re
import os
import sys
import unittest

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)

# --- Non-native python libraries in this source tree
from at4lara.models.RisDataModel import RisDataModel
from at4lara.models.RisDataModel import refTypes
from at4lara.models.RisDataModel import refTags
 

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
        i = 0
        for item in dir(self.rdm):
            if re.match("^get", item):
                i = i + 1
        
        keylen = len(self.rTa.keys())
        self.assertTrue(i == keylen, "getters (" + str(i) + ") don't equal the number of tags (" + str(keylen) + ")...")

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
        i = 0
        for item in dir(self.rdm):
            if re.match("^set", item):
                i = i + 1
        
        keylen = len(self.rTa.keys())
        self.assertTrue(i == keylen, "getters (" + str(i) + ") don't equal the number of tags (" + str(keylen) + ")...")

    # ---------------
 
    def test_refTagGetterSetterMatches_01(self):
        """
        make sure that every getter has a setter match.
        """
        gettrs = []
        for item in dir(self.rdm):
            if re.match("^get", item):
                gettrs.append(item)
        settrs = []
        for item in dir(self.rdm):
            if re.match("^set", item):
                settrs.append(item)
        for item in gettrs:
            newItem = re.sub("get", "set", item)
            self.assertTrue(newItem in settrs, "item " + item + " in setters")
 
    def test_refTagSetterGetterMatches_01(self):
        """
        make sure that every getter has a setter match.
        """
        gettrs = []
        for item in dir(self.rdm):
            if re.match("^get", item):
                gettrs.append(item)
        settrs = []
        for item in dir(self.rdm):
            if re.match("^set", item):
                settrs.append(item)
        for item in settrs:
            newItem = re.sub("set", "get", item)
            self.assertTrue(newItem in gettrs, "item " + item + " in getters")

###############################################################################


if __name__ == "__main__":
    unittest.main()




