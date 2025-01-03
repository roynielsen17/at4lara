"""
Generic class based utilities for python testing...

@author: Roy Nielsen
"""
#--- Native python libraries

import os
import io
import re
import sys
import random
import tempfile
import traceback
import inspect
import unittest
import ctypes
from datetime import datetime
#sys.path.append("../")

#--- non-native python libraries in this source tree
from at4lara.lib.getLibc import getLibc
from at4lara.lib.loggers import CyLogger
from at4lara.lib.loggers import LogPriority as lp


class LibcNotAvailableError(BaseException):
    """
    Custom Exception
    """
    def __init__(self, *args, **kwargs):
        BaseException.__init__(self, *args, **kwargs)


class GenericTestUtilities(object):
    """
    Generic class based Yutilities for ramdisk testing...
    
    @author: Roy Nielsen
    """
    def __init__(self):
        """
        Initialization Method...
        """
        self.logger = CyLogger()
        
        self.getLibc()
    ################################################
    ##### Helper Methods
    @classmethod
    def getLibc(self):
        """
        """
        #####
        # For Mac
        try:
            libc = ctypes.CDLL("/usr/lib/libc.dylib")
            # libc = ctypes.CDLL("libc.dylib")
        except OSError:
            #####
            # For Linux
            possible_paths = ["/lib/x86_64-linux-gnu/libc.so.6",
                              "/lib/i386-linux-gnu/libc.so.6",
                              "/usr/lib64/libc.so.6"]
            for path in possible_paths:
    
                if os.path.exists(path):
                    libc = ctypes.CDLL(path)
                    break
    
        try:
            if libc:
                libc.sync()
        except AttributeError:
            raise LibcNotAvailableError("............................Cannot Sync.")
    
        return libc

    ################################################

    def findLinuxLibC(self):
        """
        Find Linux Libc library...

        @author: Roy Nielsen
        """
        possible_paths = ["/lib/x86_64-linux-gnu/libc.so.6",
                          "/lib/i386-linux-gnu/libc.so.6"]
        for path in possible_paths:

            if os.path.exists(path):
                self.libcPath = path
                self.libc = ctypes.CDLL(self.libcPath)
                break

    ################################################
    @classmethod
    def _pass(self):
        """
        Filler if a library didn't load properly
        """
        pass

    ################################################

    def touch(self, fname="", message_level="normal"):
        """
        Python implementation of the touch command..

        @author: Roy Nielsen
        """
        if re.match("^\s*$", str(fname)):
            self.logger.log(lp.WARNING, "Cannot touch a file without a filename....")
        else:
            try:
                fhandle = io.open(fname, "w")
            except io.BlockingIOError as err:
                self.logger.log(lp.warning, traceback.format_exc())
                self.logger.log(lp.WARNING, "Cannot open to touch: " + str(fname))
            except io.UnsupportedOperation as err:
                self.logger.log(lp.warning, traceback.format_exc())
                self.logger.log(lp.WARNING, "Cannot open to touch: " + str(fname))
            else:
                fhandle.close() 

    ################################################

    def mkdirs(self, path=""):
        """
        A function to do an equivalent of "mkdir -p"
        """
        if not path:
            self.logger.log(lp.WARNING, "Bad path...")
        else:
            if not os.path.exists(str(path)):
                try:
                    os.makedirs(str(path))
                except OSError as err1:
                    self.logger.log(lp.WARNING, traceback.format_exc())
                    self.logger.log(lp.WARNING, "Exception: " + str(err1))
        if not path:
            self.logger.log(lp.WARNING, "Bad path...")
        else:
            if not os.path.exists(str(path)):
                try:
                    os.makedirs(str(path))
                except OSError as err1:
                    self.logger.log(lp.WARNING, "OSError exception attempting to create directory: " + str(path))
                    self.logger.log(lp.WARNING, "Exception: " + str(err1))
                except Exception as err2:
                    self.logger.log(lp.WARNING, "Unexpected Exception trying to makedirs: " + str(err2))

    ################################################

    def mkfile(self, file_path="", file_size=0, pattern="rand", block_size=512, mode=0o777):
        """
        Create a file with "file_path" and "file_size".  To be used in
        file creation benchmarking - filesystem vs ramdisk.

        @parameter: file_path - Full path to the file to create
        @parameter: file_size - Size of the file to create, in Mba
        @parameter: pattern - "rand": write a random pattern
                              "0xXX": where XX is a hex value for a byte
        @parameter: block_size - size of blocks to write in bytes
        @parameter: mode - file mode, default 0o777

        @returns: time in miliseconds the write took

        @author: Roy Nielsen
        """
        total_time = 0
        if file_path and file_size:
            self.libc.sync()
            file_size = file_size * 1024 * 1024
            if os.path.isdir(file_path):
                tmpfile_path = os.path.join(file_path, "testfile")
            else:
                tmpfile_path = file_path
            self.logger.log(lp.DEBUG, "Writing to: " + tmpfile_path)
            try:
                # Get the number of blocks to create
                blocks = file_size//block_size

                # Start timer in miliseconds
                start_time = datetime.now()

                # do low level file access...
                with os.fdopen(os.open(tmpfile_path, os.O_WRONLY | os.O_CREAT), 'w') as tmpfile_fd:

                    # do file writes...
                    for i in range(blocks):
                        tmp_buffer = os.urandom(block_size)
                        tmpfile_fd.write(str(tmp_buffer))
                        # tmpfile_fd.fsync()
                    self.libc.sync()
                os.unlink(tmpfile_path)
                self.libc.sync()

                # capture end time
                end_time = datetime.now()
            except Exception as err:
                self.logger.log(lp.WARNING, traceback.format_exc())
                self.logger.log(lp.WARNING, "Exception trying to write temp file for "  + \
                                "benchmarking...")
                self.logger.log(lp.WARNING, "Exception thrown: " + str(err))
                total_time = 0
            else:
                total_time = end_time - start_time
        return total_time
