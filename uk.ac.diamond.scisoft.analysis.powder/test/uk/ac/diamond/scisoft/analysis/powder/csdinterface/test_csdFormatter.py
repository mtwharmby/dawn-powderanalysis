import unittest

from collections import namedtuple

class csdFormatterTestCase(unittest.TestCase):
    import csdFormatter
    def setUp(self):
        pass
    
class NamedTupleToListTestCase(csdFormatterTestCase):
    self.cellAngles = namedtuple('CellAngles', [90, 105.6, 90])
    
    def runTest(self):
        self.deNamedTuple = csdFormatter.namedTuple2List(self.cellAngles)
        self.assertEqual(self.deNamedTuple, [90, 105.6, 90])

class ListToNamedTuple(csdFormatterTestCase):
    self.cellAngles = [90, 105.6, 90]
    
    def runTest(self):
        self.caAsNamedTuple = csdFormatter.list2NamedTuple(self.cellAngles)
        self.assertEqual(self.caAsNamedTuple, 'CellAngles', [90, 105.6, 90])
        