from collections import namedtuple

def namedTuple2List(inputTuple):
    return list(inputTuple)

def list2NamedTuple(inputList, name=None, fieldNames=None):
    if name == None:
        name = "No Name"
        
    namedTupleObject = namedtuple(name, fieldNames)
    
    def populateNamedTuple(args):
        return namedTupleObject(*args)
           
    return populateNamedTuple(inputList)