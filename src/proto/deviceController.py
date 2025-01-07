#!/usr/bin/env -S python -u
"""
prototyping the device controller for modules of the at4lara machine.

@author: Roy Nielsen
@note Initial working model: 1/2/2021
"""
#--- Native python libraries
import os
import re
import sys
import traceback

from optparse import OptionParser, SUPPRESS_HELP, OptionValueError, Option

sys.path.append("..")

from at4lara.lib.loggers import CyLogger
from at4lara.lib.loggers import LogPriority as lp

###############################################################################

class DeviceController(object):
	
	devices = {}
	
    def __init__(self, logger):

        if logger:
            self.logger = logger
        else:
            self.logger = CyLogger()
        self.prefix = []

    def setControllerId(self, controllerId):
		"""
		"""
		self.controllerId = controllerId
		
	def setDeviceId(self, deviceId):
		"""
		"""
		self.deviceId = deviceId
		
	def validateDevice(self, device=""):
		"""
		"""
		pass

	def addDevice(self, device):
		"""
		"""
		pass

    def printControllerDeviceState(self, logger=False, console=False, message = ""):
        """
        Log / Print Controller Device State
 
        logger: this variable is the lp.XXXX value that the programmer
                wants the message to be printed at.
        console: this variable is true/false, whether or not the 
                 message should be printed at the consle.
        """
        if logger:
            self.logger.log(logger, "Controller Device State: " + message)
        if console:
            print("Controller Device State: " + str(message))

    def printStateMachineDeviceState(self, logger=False, console=False):
        """
        Log / Print State Machine Device State
         
        logger: this variable is the lp.XXXX value that the programmer
                wants the message to be printed at.
        console: this variable is true/false, whether or not the 
                 message should be printed at the consle.
        """
        if logger:
            self.logger.log(logger, "State Machine Device State: " + message)
        if console:
            print("State Machine Device State: " + str(message))

    def printIoDeviceState(self, logger=False, console=False):
        """
        Log / Print I/O Device State

        logger: this variable is the lp.XXXX value that the programmer
                wants the message to be printed at.
        console: this variable is true/false, whether or not the 
                 message should be printed at the consle.
        """
        if logger:
            self.logger.log(logger, "I/O Device State: " + message)
        if console:
            print("I/O Device State: " + str(message))



###############################################################################

# Get all of the possible options passed in to OptionParser that are passed
# in with the -m or --modules flag
class ModulesOption(Option):

    ACTIONS = Option.ACTIONS + ("extend",)
    STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
    TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)
    ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

    def take_action(self, action, dest, opt, value, values, parser):
        if action == "extend":
            lvalue = value.split(",")
            values.ensure_value(dest, []).extend(lvalue)
        else:
            Option.take_action(
                self, action, dest, opt, value, values, parser)

###############################################################################


if __name__ == "__main__":
    """
    Executes if this file is run.
    """

    VERSION="0.4.0"
    description = "Generic test runner."
    parser = OptionParser(option_class=ModulesOption,
                          usage='usage: %prog [OPTIONS]',
                          version='%s' % (VERSION),
                          description=description)

    parser.add_option("-a", "--all-automatable", action="store_true", dest="all",
                      default=False, help="Run all tests except interactive tests.")

    parser.add_option("-v", "--verbose", action="store_true",
                      dest="verbose", default=False, \
                      help="Print status messages")

    parser.add_option("-d", "--debug", action="store_true", dest="debug",
                      default=False, help="Print debug messages")

    parser.add_option('-p', '--prefix', action="extend", type="string",
                      dest='prefix', default=[],
                      help="Collect tests with these prefixes")

    parser.add_option('-m', '--modules', action="extend", type="string",
                      dest='modules', default=[], help="Name of the test" +
                      " to run.  May indicate multiple tests to run," +
                      " if this switch is used multiple times, each with" +
                      " different test name")

    parser.add_option("-s", "--skip", action="store_true", 
                      dest="skip_syslog", default=False,
                      help="Skip syslog logging so we don't fill up the logs." + \
                           "This will leave an incremental log by default in " + \
                           "/tmp/<uid>.stonixtest.<log number>, where log number" +\
                           " is the order of the last ten stonixtest runs")

    if len(sys.argv) == 1:
        parser.parse_args(['--help'])
    options, __ = parser.parse_args()

    #####
    # Options processing

    #####
    # ... processing modules ...
    if options.all:
        modules = None
    elif options.modules:
        modules = options.modules
    else:
        modules = None

    #####
    # ... processing logging options...
    if options.verbose:
        level = 20
    elif options.debug:
        level = 10
    else:
        level = 30

    logger = CyLogger(level=level)
    logger.initializeLogs(filename="moduleDeviceController")


    #####
    # Before attempt to run
    logger.log(lp.INFO, " Before run, setting up for : ")

    #####
    # Attempting to run
    logger.log(lp.INFO, "Attempting to run: " )

    #####
    # Attempted to run, returned:
    logger.log(lp.INFO, "Finished and returned: ")


 
