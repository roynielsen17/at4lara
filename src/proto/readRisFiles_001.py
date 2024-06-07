#!/usr/bin/env -S python -u
"""
"""
import os
import re
import sys
import json
import traceback

print(__file__)

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])

print(appendDir)
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")





sys.path.append("/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1]))

print(".")
print(".")
print(".")
print(".")
print(".")

# --- Non-native python libraries in this source tree
from at4lara.lib.loggers import CyLogger
from at4lara.lib.loggers import LogPriority as lp
from at4lara.lib.loggers import LogPriority as logPriority


class RisStuff():

    RisData={}

    def __init__(self):
        """
        Initialization Method...
        """
        self.logger = CyLogger()
        
    def readExistingRisFile(self, fname=''):
        '''
        Reads in an existing RIS file 
        '''
        i = 1
        if fname:
            tmpRisObj = {}
            try:
                tmpRisDataFile = open(str(fname), 'r')
            except Exeption as err:
                trace = traceback.format_exc()
                self.logger.log(lp.INFO, str(trace))
                raise(err)
            else:
                for line in tmpRisDataFile:
                    if re.match(r"^\s+$", line):
                        #print(self.RisData)
                        #return self.RisData
                        tmpRisObj = {i : tmpRisObj}
                        self.RisData.update(tmpRisObj)
                        i = i + 1
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


#####
# ZotOut/python-Western.ris

if __name__ == "__main__" : 

    rs = RisStuff()

    risData = rs.readExistingRisFile("ZotOut/python-Western.ris")

    print(json.dumps(risData, indent=4))

    print(".")
    print(".")
    print(".")
    print("Done")
    print(".")
    print(".")
    print(".")
 
