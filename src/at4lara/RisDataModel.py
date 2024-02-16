

refTypes = { "ABST": "Abstract",
  "ANCIENT" : "Ancient Text",
  "BLOG" : "Blog",
  "BOOK" : "Book",
  "CASE" : "Legal case and case notes",
  "CHAP" : "Book section/chapter",
  "COMP" : "Computer program",
  "CONF" : "Conference proceedings",
  "CPAPER" : "Conference paper",
  "EBOOK" : "Electronic Book",
  "ECHAP" : "Electronic book section",
  "EDBOOK" : "Edited book",
  "EJOUR" : "Electronic article",
  "ELEC" : "Web page / electronic citation",
  "JFULL" : "Journal/periodical (full)",
  "JOUR" : "Journal/(article)",
  "MANSCPT" : "Manuscript",
  "PAMP" : "Pamphlet",
  "PAT" : "Patent",
  "PCOMM" : "Personal communication",
  "POD" : "Podcast",
  "RPRT" : "Report",
  "WEB" : "Web page"
}

refTags = { "A1" : "Primary author, synonym of AU",
  "A2" : "Secondary author/editor/translator",
  "A3" : "Tertiary author/editor/translator",
  "A4" : "Quaternary author/editor/translator",
  "A5" : "Quinary author/compiler",
  "A6" : "Website author",
  "AB" : "Abstract or synopsis. Notes also N2",
  "AD" : "(author/editor/inventor) address, eg postal address, email, phone, “fax. Institution.",
  "DOI" : "Digital Object Identifier",
  "EP" : "Pages",
  "ET" : "Edition",
  "J1" : "Notes",
  "J2" : "Alternative title",
  "JA" : "Standard abbreviation for Journal/periodical name",
  "L1" : "File Attachments",
  "LK" : "Links",
  "N1" : "Notes",
  "N2" : "Abstract",
  "PB" : "Publisher",
  "RD" : "Retrieved Date",
  "RN" : "Research Notes",
  "SN" : "ISSN, ISBN, or report/document/patent number",
  "SR" : "Source type- Print  0  or Electronic 1 ",
  "T1" : "(Primary) Title",
  "T2" : "Secondary title",
  "TA" : "Tertiary title",
  "TT" : "Translated title",
  "TY" : "Type of reference - must be the first tag",
  "UR" : "web/URL, can be repeated for multiple tags, or multiple URLs can be entered in a semicolon separated list",
  "WT" : "Website title",
  "WV" : "Website version",
  "Y1" : "Year///Date  Primary Date/year",
  "YR" : "Publication year"
}

def valid_string():
   pass

class RisDataModel():
    """
    """
    def __init__(self):
      RISdata = { }


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
       
        
    def getL1():
        """
        “L1” : “File Attachments”
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
        RISdata["A1"] = a1
        
    def setA2(self, a2):
        """
        
        """
        RISdata["A2"] = a2
        
        
    def setA3(self, a3):
        """
        
        """
        RISdata["A3"] = a3
        
        
    def setA4(self, a4):
        """
        
        """
        RISdata["A4"] = a4
        
        
    def setA5(self, a5):
        """
        
        """
        RISdata["A5"] = a5
        
        
    def setA6(self, a6):
        """
        
        """
        RISdata["A6"] = a6
        
        
    def setAB(self, ab):
        """
        
        """
        RISdata["AB"] = ab
        
        
    def setAD(self, ad):
        """
        
        """
        RISdata["AD"] = ad
        
        
    def setDOI(self, doi):
        """
        
        """
        RISdata["DOI"] = doi
        
        
    def setEP(self, ep):
        """
        
        """
        RISdata["EP"] = ep
        
        
    def setET(self, et):
        """
        
        """
        RISdata["ET"] = et
        
        
    def setJ1(self, j1):
        """
        
        """
        RISdata["J1"] = j1
        
        
    def setJ2(self, j2):
        """
        
        """
        RISdata["J2"] = j2
        
        
    def setJA(self, ja):
        """
        
        """
        RISdata["JA"] = ja
        
        
    def setL1(self, l1):
        """
        
        """
        RISdata["L1"] = l1
        
        
    def setLK(self, lk):
        """
        
        """
        RISdata["LK"] = lk
        
        
    def setN1(self, n1):
        """
        
        """
        RISdata["N1"] = n1
        
        
    def setN2(self, n2):
        """
        
        """
        RISdata["N2"] = n2
        
        
    def setPB(self, pb):
        """
        
        """
        RISdata["PB"] = pb
        
        
    def setRD(self, rd):
        """
        
        """
        RISdata["RD"] = rd
        
        
    def setRN(self, rn):
        """
        
        """
        RISdata["RN"] = rn
        
        
    def setSN(self, sn):
        """
        
        """
        RISdata["SN"] = sn
        
        
    def setSR(self, sr):
        """
        “SR” : “Source type- Print  0  or Electronic 1 ”
        """
        if sr != 0:
            raise(ValueError)
        elif sr != 1:
            raise(ValueError)
        else:
            self.RISdata["SR"] = sr
        
        
    def setT1(self, t1):
        """
        
        """
        RISdata["T1"] = t1
        
        
    def setT2(self, t2):
        """
        
        """
        RISdata["T2"] = t2
        
        
    def setTA(self, ta):
        """
        
        """
        RISdata["TA"] = ta
        
        
    def setTT(self, tt):
        """
        
        """
        RISdata["TT"] = tt
        
        
    def setTY(self, ty):
        """
        
        """
        if ty not in keys(refTypes):
          raise(ValueError)
        else:
          self.RISdata["TY"] = ty
        
        
    def setUR(self, ur):
        """
        
        """
        RISdata["UR"] = ur
        
        
    def setWT(self, wt):
        """
        
        """
        RISdata["WT"] = wt
        
        
    def setWV(self, wv):
        """
        
        """
        RISdata["WV"] = wv
        
        
    def setY1(self, y1):
        """
        
        """
        RISdata["Y1"] = y1
        
        
    def setYR(self, yr):
        """
        
        """
        RISdata["YR"] = yr
        
        
        
    



