#!/usr/bin/env -S python -u
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
from at4lara.helpers.getLibc import getLibc

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

class test_getLibc(unittest.TestCase):
    """
    """
    metaVars = {'setupDone': None, 'testStartTime': 0, 'setupCount': 0}
    libc = getLibc()

    ##################################

    def setUp(self):
        """
        This method runs before each test run.

        @author: Roy Nielsen
        """
        self.metaVars['setupCount'] = self.metaVars['setupCount'] + 1

        if self.metaVars['setupDone']:
            return
        #####
        # setUpClass functionality here.
        # self.libc = getLibc()
        #####
        # Start timer in miliseconds
        self.metaVars['testStartTime'] = datetime.now()
        self.metaVars['setupDone'] = True

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

    @unittest.skip("no longer cross platform")
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
        LOGGER.log(lp.INFO, str(c_system) + " : " + str(py_system))
        self.libc.sync()
        self.assertTrue(c_system == py_system, "Systems not the same...")
        self.libc.sync()
        
    ##################################

    @unittest.skip("no longer cross platform")
    def test_symlink(self):
        """
        """
        # libc = getLibc()
        pathName = os.path.dirname(sys.argv[0])
        mylink = "testlink"
        linkName = os.path.join(pathName, mylink)
        self.libc.symlink(sys.argv[0], linkName)
        self.libc.sync()
        self.libc.sync()
        self.libc.sync()
        self.assertTrue(os.path.islink(linkName), "Not a link...")
        self.libc.sync()
        # self.libc.unlink(mylink)
        self.libc.sync()

    ##################################

    def tearDown(self):
        """
        Final cleanup actions...
        """
        # libc = getLibc()
        
        self.metaVars['setupCount'] = self.metaVars['setupCount'] - 1

        #####
        # capture end time
        testEndTime = datetime.now()

        #####
        # Calculate and log how long it took...
        test_time = (testEndTime - self.metaVars['testStartTime'])
        # print str(test_time)
        # global LOGGER
        LOGGER.log(lp.INFO, self.__module__ + " took " + str(test_time) + " time so far...")
        self.libc.sync()

        if self.metaVars['setupCount'] == 0:
            #####
            # TearDownClass functionality here.
            self.libc.sync()
            # time.sleep(5)

###############################################################################


if __name__ == "__main__":
    #LOGGER.setInitialLoggingLevel(10)
    LOGGER.initializeLogs()
    unittest.main()
