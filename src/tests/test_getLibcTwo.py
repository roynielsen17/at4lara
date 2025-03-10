#!/usr/bin/env -S python -u
# ! /usr/bin/python
"""
Test for basic functionality of the basic libc
functionality provided by getLibc

@author: Roy Nielsen
"""

# --- Native python libraries

import os
import sys
import copy
import time
import platform
import unittest
import ctypes as C
from datetime import datetime

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)

# --- Non-native python libraries in this source tree
from at4lara.helpers.loggers import CyLogger
from at4lara.helpers.loggers import LogPriority as lp

if sys.platform.startswith("darwin"):
    from at4lara.helpers.getLibc.macGetLibc import getLibc
elif sys.platform.startswith("linux"):
    from at4lara.helpers.getLibc.linuxGetLibc import getLibc
elif sys.platform.startswith("win32"):
    from at4lara.helpers.getLibc.winGetLibc import getLibc
else:
    raise Exception("Damn it Jim!!! What OS is this???")


LOGGER = CyLogger()
#LOGGER.setInitialLoggingLevel(30)

class test_getLibcTwo(unittest.TestCase):
    """
    """
    libc = getLibc()

    ##################################

    @unittest.skip("not applicable here...")
    def test_get_euid(self):
        """
        """
        # libc = getLibc()
        c_euid = self.libc.geteuid()
        py_euid = os.geteuid()
        self.assertEqual(c_euid, py_euid, "Euid's are not equal...")

    ##################################
    @unittest.skip("Someone 'fixed' the test, and broke it.  Possibly no longer linux-macOS cross platform")
    def test_uname(self):
        """
        """
        # libc = getLibc()
        class uts_struct(C.Structure):
            _fields_ = [ ('sysname', C.c_char * 65),
                         ('nodename', C.c_char * 65),
                         ('release', C.c_char * 65),
                         ('version', C.c_char * 65),
                         ('machine', C.c_char * 65),
                         ('domain', C.c_char * 65) ]
        tmpStruct = uts_struct()
        self.libc.uname(C.byref(tmpStruct))
        c_system = copy.deepcopy(tmpStruct.sysname.strip())
        py_system = platform.system()
        self.libc.sync()
        self.assertTrue(c_system == py_system, "Systems not the same...")
        # self.libc.free(C.byref(tmpStruct))
        self.libc.sync()
        self.libc.sync()
        
    ##################################
    @unittest.skip("need to re-work test, looks like someone 'fixed' the test and broke it...")
    def test_symlink(self):
        """
        """
        # libc = getLibc()
        pathName = os.path.dirname(sys.argv[0])
        mylink = "testlink"
        linkName = os.path.join(pathName, mylink)
        self.libc.symlink(sys.argv[0], linkName)
        self.libc.sync()
        self.assertTrue(os.path.islink(linkName), "Not a link...")
        self.libc.sync()
        # self.libc.unlink(mylink)
        self.libc.sync()
        self.libc.sync()

###############################################################################


if __name__ == "__main__":
    LOGGER.setInitialLoggingLevel(30)
    unittest.main()
