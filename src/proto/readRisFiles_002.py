#!/usr/bin/env -S python -u
"""
"""
import os
import re
import sys
import json
import traceback

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)

# --- Non-native python libraries in this source tree
from at4lara.helpers.loggers import CyLogger
from at4lara.helpers.loggers import LogPriority as lp
from at4lara.helpers.loggers import LogPriority as logPriority


class RisStuff():

    RisData={}
    i = 1

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
            except Exeption as err:
                trace = traceback.format_exc()
                self.logger.log(lp.INFO, str(trace))
                raise(err)
            else:
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


#####
# ZotOut/python-Western.ris

if __name__ == "__main__" : 

    rs = RisStuff()

    # risData = rs.readExistingRisFile("ZotOut/python-Western.ris")
    rs.readExistingRisFile("ZotOut/python-Western.ris")
    risData = rs.readExistingRisFile("ZotOut/WindCatchers-Western.ris")

    print(json.dumps(risData, indent=4))

    print(".")
    print(".")
    print(".")
    print("Done")
    print(".")
    print(".")
    print(".")
 
