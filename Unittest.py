import sys
import unittest
from io import StringIO
from unittest.mock import patch

from ChooseNumberOfClasses import chooseClasses


class ChooseNumberOfClasses(unittest.TestCase):
    def testNegative(self):
        self.assertRaises(ValueError)

    def testLargeNumber(self):
        self.assertRaises(ValueError)

    def testStringInput(self):
        self.assertRaises(ValueError)

testCourses = [
         {"Class Name": "CS222", "Class Section": "574", "Meeting Days": "TR", "Start Time": "1500", "End Time": "1650"},
         {"Class Name": "CS222", "Class Section": "996", "Meeting Days": "MWF", "Start Time": "1530", "End Time": "1815"},
         {"Class Name": "MATH166", "Class Section": "007", "Meeting Days": "MWF", "Start Time": "1100", "End Time": "1345"}
        ]

class TestChooseClasses(unittest.TestCase):
    @patch('builtins.input', sideEffect=["CS222"])
    def testPrintAllSections(self, mocked_input):
        printedClasses = StringIO()
        sys.stdout = printedClasses
        chooseClasses(1, testCourses)
        sys.stdout = sys.__stdout__
        output = printedClasses.getvalue()
        self.assertIn("Available sections for CS222:", output)
        self.assertIn("1. Section 574", output)
        self.assertIn("2. Section 996", output)

if __name__ == '__main__':
    unittest.main()