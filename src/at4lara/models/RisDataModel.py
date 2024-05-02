#!/usr/bin/env -S python -u


import os
import sys

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)

# --- Non-native python libraries in this source tree
from at4lara.models.refs.RisRefs import refTags, refTypes

def valid_string():
    pass

class RisDataModel():
    """
    """
    RISdata = { }

    def __init__(self):
        self.RISdata = {}

    def getA1(self):
        """
        “A1” : "Primary author, synonym of AU”
        """
        return self.RISdata["A1"]

    def getA2(self):
        """
        “A2” : “Secondary author/editor/translator”
        """
        return self.RISdata["A2"]
 
    def getA3(self):
        """
        “A3” : “Tertiary author/editor/translator”
        """
        return self.RISdata["A3"]

    def getA4(self):
        """
        “A4” : “Quaternary author/editor/translator”
        """
        return self.RISdata["A4"]
 
    def getA5(self):
        """
        “A5” : “Quinary author/compiler”
        """
        return self.RISdata["A5"]

    def getA6(self):
        """
        “A6” : “Website author”
        """
        return self.RISdata["A6"]

    def getAB(self):
        """
        “AB” : “Abstract or synopsis. Notes also N2”
        """
        return self.RISdata["AB"]

    def getAD(self):
        """
        “AD” : “(author/editor/inventor) address, eg postal address, email, phone, “fax. Institution.”
        """
        return self.RISdata["AD"]

    def getDOI(self):
        """
        “DOI” : “Digital Object Identifier”
        """
        return self.RISdata["DOI"]

    def getEP(self):
        """
        “EP” : “Pages”
        """
        return self.RISdata["EP"]

    def getET(self):
        """
        “ET” : “Edition”
        """
        return self.RISdata["ET"]

    def getJ1(self):
        """
        “J1” : “Notes”
        """
        return self.RISdata["J1"]

    def getJ2(self):
        """
        “J2” : “Alternative title”
        """
        return self.RISdata["J2"]

    def getJA(self):
        """
        “JA” : “Standard abbreviation for Journal/periodical name”
        """
        return self.RISdata["JA"]

    def getL1(self):
        """
        “L1” : “File Attachments"
        """
        return self.RISdata["L1"]

    def getLK(self):
        """
        “LK” : “Links”
        """
        return self.RISdata["LK"]

    def getN1(self):
        """
        “N1” : “Notes”
        """
        return self.RISdata["N1"]

    def getN2(self):
        """
        “N2” : “Abstract”
        """
        return self.RISdata["N2"]       

    def getPB(self):
        """
        “PB : “Publisher”
        """
        return self.RISdata["PB"]       

    def getRD(self):
        """
        “RD” : “Retrieved Date”
        """
        return self.RISdata["RD"]       

    def getRN(self):
        """
        “RN” : “Research Notes”
        """
        return self.RISdata["RN"]

    def getSN(self):
        """
        “SN” : “ISSN, ISBN, or report/document/patent number”
        """
        return self.RISdata["SN"]       

    def getSR(self):
        """
        “SR” : “Source type- Print  0  or Electronic 1 ”
        """
        return self.RISdata["SR"]       

    def getT1(self):
        """
        “T1” : “(Primary) Title”
        """
        return self.RISdata["T1"]       

    def getT2(self):
        """
        “T2” : “Secondary title”
        """
        return self.RISdata["T2"]       

    def getTA(self):
        """
        “TA” : “Tertiary title”
        """
        return self.RISdata["TA"]       

    def getTT(self):
        """
        “TT” : “Translated title”
        """
        return self.RISdata["TT"]       

    def getTY(self):
        """
        ““TY” : Type of reference - must be the first tag”
        """
        return self.RISdata["TY"]       

    def getUR(self):
        """
        “UR” : “web/URL, can be repeated for multiple tags, or multiple URLs can be entered in a semicolon separated list”
        """
        return self.RISdata["UR"]       

    def getWT(self):
        """
        "WT" : “Website title”
        """
        return self.RISdata["WT"]       

    def getWV(self):
        """
        "WV : “Website version”
        """
        return self.RISdata["WV"]       

    def getY1(self):
        """
        "Y1" : “Year///Date  Primary Date/year”
        """
        return self.RISdata["Y1"]       

    def getYR(self):
        """
        "YR" : “Publication year”
        """
        return self.RISdata["YR"]       

    ############### setters #########################        

    def setA1(self, a1):
        """
        
        """
        self.RISdata["A1"] = a1
 
    def setA2(self, a2):
        """
        
        """
        self.RISdata["A2"] = a2
 
    def setA3(self, a3):
        """
        
        """
        self.RISdata["A3"] = a3
 
    def setA4(self, a4):
        """
        
        """
        self.RISdata["A4"] = a4

    def setA5(self, a5):
        """
        
        """
        self.RISdata["A5"] = a5
 
    def setA6(self, a6):
        """
        
        """
        self.RISdata["A6"] = a6

    def setAB(self, ab):
        """
        
        """
        self.RISdata["AB"] = ab

    def setAD(self, ad):
        """
        
        """
        self.RISdata["AD"] = ad

    def setDOI(self, doi):
        """
        
        """
        self.RISdata["DOI"] = doi

    def setEP(self, ep):
        """
        
        """
        self.RISdata["EP"] = ep

    def setET(self, et):
        """
        
        """
        self.RISdata["ET"] = et

    def setJ1(self, j1):
        """
        
        """
        self.RISdata["J1"] = j1

    def setJ2(self, j2):
        """
        
        """
        self.RISdata["J2"] = j2

    def setJA(self, ja):
        """
        
        """
        self.RISdata["JA"] = ja

    def setL1(self, l1):
        """
        
        """
        self.RISdata["L1"] = l1

    def setLK(self, lk):
        """
        
        """
        self.RISdata["LK"] = lk

    def setN1(self, n1):
        """
        
        """
        self.RISdata["N1"] = n1

    def setN2(self, n2):
        """
        
        """
        self.RISdata["N2"] = n2

    def setPB(self, pb):
        """
        
        """
        self.RISdata["PB"] = pb

    def setRD(self, rd):
        """
        
        """
        self.RISdata["RD"] = rd

    def setRN(self, rn):
        """
        
        """
        self.RISdata["RN"] = rn

    def setSN(self, sn):
        """
        
        """
        self.RISdata["SN"] = sn

    def setSR(self, sr):
        """
        “SR” : “Source type- Print  0  or Electronic 1 ”
        """
        assert(sr==0 or sr==1), "Only Zero or One"
        if sr == 0 or sr == 1:
            self.RISdata["SR"] = sr

    def setT1(self, t1):
        """
        
        """
        self.RISdata["T1"] = t1

    def setT2(self, t2):
        """
        
        """
        self.RISdata["T2"] = t2

    def setTA(self, ta):
        """
        
        """
        self.RISdata["TA"] = ta

    def setTT(self, tt):
        """
        
        """
        self.RISdata["TT"] = tt

    def setTY(self, ty):
        """
        
        """
        if ty not in self.RISdata.keys(refTypes):
          raise(ValueError)
        else:
          self.RISdata["TY"] = ty

    def setUR(self, ur):
        """
        
        """
        self.RISdata["UR"] = ur

    def setWT(self, wt):
        """
        
        """
        self.RISdata["WT"] = wt

    def setWV(self, wv):
        """
        
        """
        self.RISdata["WV"] = wv

    def setY1(self, y1):
        """
        
        """
        self.RISdata["Y1"] = y1

    def setYR(self, yr):
        """
        
        """
        self.RISdata["YR"] = yr

