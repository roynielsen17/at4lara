#!/usr/bin/env -S python -u
"""
"""
import os
import re
import sys
import glob
import json
import traceback

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-3])
sys.path.append(appendDir)

# --- Non-native python libraries in this source tree
from at4lara.lib.loggers import CyLogger
from at4lara.lib.loggers import LogPriority as lp
from at4lara.lib.loggers import LogPriority as logPriority


class ReadRisData():

    RisData={}
    i = 0

    def __init__(self):
        """
        Initialization Method...
        """
        self.logger = CyLogger()
       
    def readExistingRisFile(self, fname=''):
        '''
        Reads in an existing RIS file 
        '''

        if fname:
            tmpRisObj = {}
            try:
                tmpRisDataFile = open(str(fname), 'r')
            except Exception as err:
                trace = traceback.format_exc()
                self.logger.log(lp.INFO, str(trace))
                raise(err)
            else:
                #####
                # Assumes starting with new RIS block
                self.i = self.i + 1
                for line in tmpRisDataFile:
                    if re.match(r"^\s+$", line):
                        #print(self.RisData)
                        #return self.RisData
                        tmpRisObj = {self.i : tmpRisObj}
                        self.RisData.update(tmpRisObj)
                        self.i = self.i + 1
                        tmpRisObj = {}
                    try:
                        label, variable = line.split("  - ")
                        #print(label + "  :  " + variable)
                        newdatadict = {label.strip() : variable.strip()}
                        tmpRisObj.update(newdatadict)
                    except ValueError:
                        # found an empty line - which is the separator between RIS objects
                        pass
                    except Exception as err:
                        trace = traceback.format_exc()
                        self.logger.log(str(lp.INFO), str(trace))
                        #print(str(err))
                        # break
                        raise(err)
                    #print("==============")
                    # print(tmpRisObj)
                #return self.RisData
            finally:
                try:
                    tmpRisDataFile.close()
                except:
                    pass
        return self.RisData

    def readRisStringData(self, stringBlock=""):
        """
        """
        #####
        # Assumes starting with new RIS block
        self.i = self.i + 1
        for line in stringBlock:
            if re.match(r"^\s+$", line):
                #print(self.RisData)
                #return self.RisData
                try:
                    tmpRisObj = {self.i : tmpRisObj}
                    self.RisData.update(tmpRisObj)
                    self.i = self.i + 1
                    tmpRisObj = {}
                except UnboundLocalError:
                    pass
            try:
                label, variable = line.split("  - ")
                #print(label + "  :  " + variable)
                newdatadict = {label.strip() : variable.strip()}
                tmpRisObj.update(newdatadict)
            except ValueError:
                # found an empty line - which is the separator between RIS objects
                pass
            except Exception as err:
                trace = traceback.format_exc()
                self.logger.log(str(lp.INFO), str(trace))
                #print(str(err))
                # break
                raise(err)
   
    def readMyRisData(self):
        """
        """
        return self.RisData


#####
# ZotOut/python-Western.ris

if __name__ == "__main__" : 

    rs = ReadRisData()
    risData = {}
    # risData = rs.readExistingRisFile("ZotOut/python-Western.ris")
    # rs.readExistingRisFile("ZotOut/python-Western.ris")
    # risData = rs.readExistingRisFile("ZotOut/WindCatchers-Western.ris")
    path2search = './ZotOut'
    for myfile in glob.glob(path2search + '/*.ris'):
        print(str(myfile))
        rs.readExistingRisFile(myfile)

    risData = rs.readMyRisData()
    print(json.dumps(risData, indent=4))


    print("=============")
    print("-------------")
    print("=============")

    ris = ReadRisData()
    risData = {}
    path2search = './ZotOut'
    for myfile in glob.glob(path2search + '/*.ris'):
        print(myfile)
        try:
            with open(myfile, 'r') as tmpMyRisDataFile:
                file_content = tmpMyRisDataFile.read()
        except Exception as err:
            trace = traceback.format_exc()
            print(str(trace))
            raise(err)
        else:
            print(file_content)
            ris.readRisStringData(file_content)

    risData = rs.readMyRisData()
    print(json.dumps(risData, indent=4))


    print("=============")
    print("-------------")

    print(".")
    print(".")
    print(".")
    print("Done")
    print(".")
    print(".")
    print(".")


