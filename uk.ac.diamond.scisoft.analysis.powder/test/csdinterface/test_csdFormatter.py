import unittest

from collections import namedtuple

#Need to import the package
import csdinterface
#And need to import each of the modules to test too
from csdinterface import csdFormatter

class csdFormatterTestCase(unittest.TestCase):
    def setUp(self):
        self.tupleName = 'CellAngles'
        self.tupleFieldNames = ['al', 'be', 'ga']
        self.cellAnglesValues = [90, 105.6, 90]
        self.cellAngleNamedTuple = namedtuple(self.tupleName, self.tupleFieldNames)
        
        self.cA = self.cellAngleNamedTuple(al=self.cellAnglesValues[0], be=self.cellAnglesValues[1], ga=self.cellAnglesValues[2])
    
class NamedTupleToListTestCase(csdFormatterTestCase):    
    def runTest(self):
        self.deNamedTuple = csdinterface.csdFormatter.namedTuple2List(self.cA)
        self.assertEqual(self.deNamedTuple, self.cellAnglesValues)

class ListToNamedTuple(csdFormatterTestCase):
    def runTest(self):
        self.caAsNamedTuple = csdinterface.csdFormatter.list2NamedTuple(self.cellAnglesValues, name = "CellAngles", fieldNames = ["al", "be", "ga"])
        self.assertEqual(self.caAsNamedTuple, self.cA)