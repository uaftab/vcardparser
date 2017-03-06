#!/usr/bin/env python3

#System level imports
import sys
import argparse

#Imports
import vcard

#Globals .... hisss
spacer = "    "
#defs
vcard_begin = "BEGIN:VCARD\n"
vcard_end    = "END:VCARD\n"
linespervcardobject = 8

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
        if line == vcard_end: # Are we at the end section of object
            accumulate = False
            vcardobjs.append(obj)
            obj = [] # reset object to empty
    if accumulate:
        print("Malformed vcard obj file missing %s",vcard_end)
        print (obj)
        sys.exit(-1)
    return vcardobjs

def parsingsanitycheck(Numoflinesreadfromfile,Numofobjesctsparsed):
    if ((Numoflinesreadfromfile/Numofobjesctsparsed) == linespervcardobject): 
        print(spacer,"[OK] - Parsing sanity check passed. - Each vcard object is composed of",linespervcardobject)
    else:
        print(spacer,"[XX] - Num of objs parsed wrt to lines parsed is not whole")

    return

def buildvcardobjs(parsedobjs):
    vcardlist = []
    for i,item in enumerate(parsedobjs):
        obj = vcard.vcard(i,item)
        obj.buildvcard()
        vcardlist.append(obj)

    if len(parsedobjs) == len(vcardlist):
        return vcardlist
    else:
        print(spacer,"[XX] - Number of Parsedobjs and Built vCard objects dont match in buildvcardobjs")
        sys.exit(-1)

def uniquecontacts(vcardlist):
    uniqueset = set(vcardlist)
    return uniqueset

def comparerawoutput(vcardlist):
    thing = ""
    for item in vcardlist:
        thing = thing + item.raw
    sys.stdout.write (thing)
    sys.stdout.flush()
    return

def debugprints(vcardlist):
    for item in vcardlist:
        print("[",item.uid,"] --- ",item.name)

def parseinputs(*args,**kwargs):
    parser = argparse.ArgumentParser(description='vCard Processor')
    parser.add_argument('inputfile', nargs='+', help='input file to process')
    args = parser.parse_args()
    input_dict = {"inputfile":args.inputfile[0]} # first pos is input file 
    return input_dict

if __name__ == "__main__":
    inputs = parseinputs()
    contents = readfile(inputs['inputfile'])
    objs     = parse(contents)
    #parsingsanitycheck(len(contents),len(objs))
    vcardlist = buildvcardobjs(objs)
    #comparerawoutput(vcardlist) 
    uniquevcards = uniquecontacts(vcardlist)
    #debugprints(uniquevcards)
    #comparerawoutput(uniquevcards)
    print ("VcardsInput:",len(vcardlist))
    print ("Unique:",len(uniquevcards))
