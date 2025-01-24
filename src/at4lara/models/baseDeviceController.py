#!/usr/bin/env -S python -u
"""
prototyping the device controller for modules of the at4lara machine.

"""
#--- Native python libraries
import os
import re
import sys
import inspect
import traceback

from optparse import OptionParser, SUPPRESS_HELP, OptionValueError, Option

appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-2])

from at4lara.helpers.loggers import CyLogger
from at4lara.helpers.loggers import LogPriority as lp

###############################################################################
# Exception setup

class NotAValidDeviceError(Exception):
    """
    Custom Exception
    """
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class SpecialDevicesCannotUnloadError(Exception):
    """
    Custom Exception
    """
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

###############################################################################

class DeviceController(object):
    """
    """

    devices = {}

    def __init__(self, logger):

        if logger:
            self.logger = logger
        else:
            self.logger = CyLogger()
        self.prefix = []

        self.deviceControllerId = MainModelControllerId_00001
        self.deviceClassId = ModelClassId_00001
        self.deviceId = MainModelClassId_00001
        self.concreteDeviceId = 0x00001
        self.mainControllerId = 0x00001

    def setControllerId(self, controllerId):
        """
        """
        self.controllerId = controllerId

    def setDeviceClassId(self, deviceClassId):
        """
        """
        self.deviceClassId = deviceClassId

    def setDeviceId(self, deviceId):
        """
        """
        self.deviceId = deviceId

    def setConcreteDeviceId(self, concreteDeviceId):
        """
        """
        self.concreteDeviceId = concreteDeviceId

    def validateDeviceAdd(self, device=""):
        """
        """
        status = False
        if isinstance(device, str):
            status = True
        else:
            raise NotAValidDeviceError("Sorry, you have not supplied a valid device")
        return status

    def addDevice(self, device):
        """
        """
        if self.validateDeviceAdd(device):
            self.devices[device] = device

    def validateDeviceRemoval(self, device):
        """
        """
        status = False
        SpecialDevices = ["specialFileCRUD", "specialPrint", "specialIO", "specialGUI"]
        if device not in SpecialDevices and isinstance(device, str):
            status = True
        elif device in SpecialDevices:
            raise SpecialDevicesCannotUnloadError("Cannot unload Sepecial Devices")
        else:
            raise NotAValidDeviceError("Sorry, you have not supplied a valid device")
        return status

    def removeDevice(self, device):
        """
        """
        if self.validateDeviceRemoval(device):
            del self.devices[device]

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

    def printModuleIds(self, logger=False, consle=False):
        """
        """
        if logger:
            self.logger.log(logger, "deviceControllerId: " + str(self.deviceControllerId))
            self.logger.log(logger, "deviceClassId: " + str(self.deviceClassId))
            self.logger.log(logger, "deviceId: " + str(self.deviceId))
            self.logger.log(logger, "concreteDeviceId: " + str(self.concreteDeviceId))
            self.lp.log(logger, "mainControllerId: " + str(self.mainControllerId))
        if console:
            print("deviceControllerId: " + str(self.deviceControllerId))
            print("deviceClassId: " + str(self.deviceClassId))
            print("deviceId: " + str(self.deviceId))
            print("concreteDeviceId: " + str(self.concreteDeviceId))
            print("mainControllerId: " + str(self.mainControllerId))

    def printModuleMethods(self, logger=False, console=False):
        """
        """
        modules = []
        for item in dir(self.__class__):
            if not re.match(r"^__.*", item):
                modules.append(item)
        if logger:
            self.logger(logger, str(modules))
        if console:
            print(str(modules))

    def printModuleDevices(self, logger=False, console=False):
        """
        """
        if self.devices:
            if logger:
                self.logger(logger, str(self.devices))
            if console:
                print(str(self.devices))


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


 
