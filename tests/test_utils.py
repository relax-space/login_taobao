import unittest
import os
import gui_
import utils

# py.test.exe .\tests\utils.py -s

class TestUtil(unittest.TestCase):

    def testAbsPath(self):
        print(utils.absPath("tests/data"))
                
