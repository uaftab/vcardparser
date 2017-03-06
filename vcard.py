DEF_VCARD_FIELD_NAME    = "N:"
DEF_VCARD_FIELD_VERSION = "VERSION:"
DEF_VCARD_FIELD_FNAME   = "FN:"
class vcard:


    def __init__(self,uniqueid,parsedobjaslist):
        self.rep_list=parsedobjaslist
        self.uid=uniqueid
        self.fname = "INVALID"
        self.name  = "INVALID"
    def print(self):
        print("[%d] -- %s",self.pos,self.raw)

    def buildvcard(self):
        #build raw which can be flushed to file
        self.raw = ""
        for item in self.rep_list:
            self.raw=self.raw+str(item)
    
            # build some fields
            string = str(item)
            pos_name  = string.find(DEF_VCARD_FIELD_NAME)
            pos_fname = string.find(DEF_VCARD_FIELD_FNAME)
            if pos_name == 1:
                #print (pos_name)
                self.name = string[(len(DEF_VCARD_FIELD_NAME)+1):]
#                print (self.name)
            if pos_fname == 1:
                self.fname = string[len(DEF_VCARD_FIELD_FNAME)+1:]
    
    def __hash__(self):
        return hash(str(self.name))
        
    def __eq__(self,other):
        if (hash(str(self.name)) == other):
            return True
        else:
            return False
