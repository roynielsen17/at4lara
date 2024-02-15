#!/usr/bin/env -S python -u
"""
Testing logging functionality via CyLogger

@author: Roy Nielsen
"""
# --- Native python libraries
import unittest
import sys
import os

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)

# --- Non-native python libraries in this source tree
from at4lara.lib.loggers import CyLogger
from at4lara.lib.loggers import LogPriority

#####
# Set up logging
logger = CyLogger(debug_mode=True)
logger.initializeLogs()
priority = LogPriority()


class test_loggers(unittest.TestCase):
    """
    Test for the CyLogger class, based on the STONIX project's test
    for it's logdispatcher.
    """

    def testLogCritical(self):
        try:
            logger.log(priority.CRITICAL, "Critical level message")
        except:
            self.fail("Failed to write CRITICAL to log file")

    def testLogError(self):
        try:
            logger.log(priority.ERROR, "Error level message")
        except:
            self.fail("Failed to write ERROR to log file")

    def testLogWarning(self):
        try:
            logger.log(priority.WARNING, "Warning level message")
        except:
            self.fail("Failed to write WARNING to log file")

    def testLogInfo(self):
        try:
            logger.log(priority.INFO, "Info level message")
        except:
            self.fail("Failed to write INFO to log file")

    def testLogDebug(self):
        try:
            logger.log(priority.DEBUG, "Debug level message")
        except:
            self.fail("Failed to write DEBUG to log file")


###############################################################################


if __name__ == "__main__":
    unittest.main()

