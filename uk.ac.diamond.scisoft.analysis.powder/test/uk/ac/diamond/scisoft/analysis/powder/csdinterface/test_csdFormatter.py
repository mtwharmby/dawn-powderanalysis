import unittest

from collections import namedtuple

import uk.ac.diamond.scisoft.analysis.powder.csdinterface
from uk.ac.diamond.scisoft.analysis.powder.csdinterface import csdFormatter

class csdFormatterTestCase(unittest.TestCase):
    def setUp(self):
        self.cellAngleNamedTuple = namedtuple('CellAngles', [90, 105.6, 90])
        self.cellAnglesValues = [90, 105.6, 90]
    
class NamedTupleToListTestCase(csdFormatterTestCase):    
    def runTest(self):
        self.deNamedTuple = csdFormatter.namedTuple2List(self.cellAngleNamedTuple)
        self.assertEqual(self.deNamedTuple, [90, 105.6, 90])

class ListToNamedTuple(csdFormatterTestCase):
    
    def runTest(self):
        self.caAsNamedTuple = csdFormatter.list2NamedTuple(self.cellAnglesValues, name = "CellAngles", fieldNames = ["al", "be", "ga"])
        self.assertEqual(self.caAsNamedTuple, 'CellAngles', [90, 105.6, 90])
        