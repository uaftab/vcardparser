#!/usr/bin/env python3

#System level imports
import sys

#Imports
import vcard

#Globals .... hisss
vcardlist=[]

#defs
vcard_begin = "BEGIN:VCARD"
vcard_end    = "END:VCARD"


#read from file and return as list
def readfile(filename):
    #Assuming it exists
    filecontents = []
    with open(filename,'r') as file:
        for line in file:
            filecontents.append(line)


    return filecontents

def parse(filecontents):
    vcardobjs = []
    obj = []
    accumulate = False
    for line in filecontents:
        if line == vcard_begin:
            accumulate = True # Start accumulate of line into obj
        if accumulate: #Build object ? 
            obj.append(line)
        if line == vcard_end # Are we at the end section of object
            accumulate = False
            vcardobjs.append(obj)
            obj = [] # reset object to empty
    if not accumulate:
        printf("Malformed vcard obj file missing %s",vcard_end)
        sys.exit(-1)
    return vcardobjs
if __name__ == "__main__":
    contents = read('vcardfile')
    objs     = parse(contents)

    print (objs)
    print (len(objs))

