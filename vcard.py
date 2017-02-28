class vcard:


    def __init__(self,uniqueid,parsedobjaslist):
        self.rep_list=parsedobjaslist
        self.uid=uniqueid
    def print(self):
        print("[%d] -- %s",self.pos,self.raw)
