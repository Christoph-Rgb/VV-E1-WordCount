import unittest
from unittest.mock import patch
import os
import sys
from pathlib import Path
sys.path.append('/Users/cs/Dropbox/Studium/Master/Semester 3/03_VV')
from VV_E1_WordCount.InputReader import FileReader, CommandLineReader, InputReader

FILENAME = "./test.file"
INPUT = "This is a test file. It contains words that should be counted correctly. \n Hopefully it does so"
WRONG_FILENAME = "./not_existing.file"

# dummy test of the abstract class
class InputReaderTest(unittest.TestCase):
    def test(self):
        reader = InputReader()
        reader.readInput()

# tests for command line reader
class CommandLineReaderTest(unittest.TestCase):
    def test_initSucceeds(self):
        reader = CommandLineReader()

    @patch('builtins.input', lambda x: INPUT)
    def test_readInputSucceeds(self):
        reader = CommandLineReader()
        input = reader.readInput()
        self.assertEqual(INPUT, input)

# tests for file reader
class FileReaderTest(unittest.TestCase):

    # creates a test file to be read from
    def createTestFile(self):
        with open(FILENAME,"a+") as file:
            file.write(INPUT)

    # deletes the test file after every test
    def removeTestFile(self):
        try:
            os.remove(FILENAME)
        except(FileNotFoundError):
            pass

    def setUp(self):
        self.createTestFile()

    def tearDown(self):
        self.removeTestFile()
    
    def test_initSucceedsForString(self):
        fileReader = FileReader(FILENAME)

    def test_initSucceedsForPath(self):
        path = Path(FILENAME)
        fileReader = FileReader(path)

    def test_initThrowsErrorForParameterThatIsNotStringOrPath(self):
        with self.assertRaises(ValueError):
            fileReader = FileReader(4711)

    def test_initThrowsErrorForNotExistingFile(self):
        with self.assertRaises(AssertionError):
            fileReader = FileReader(WRONG_FILENAME)

    def test_readInputSucceeds(self):
        #arrange
        fileReader = FileReader(FILENAME)
        #act
        input = fileReader.readInput()
        #assert
        self.assertEqual(INPUT, input)

    def test_readInputThrowsErrorForNotAccessibleFile(self):
        #arrange
        fileReader = FileReader(FILENAME)
        self.removeTestFile()

        #act
        with self.assertRaises(FileNotFoundError):
            fileReader.readInput()

if __name__ == '__main__':
    unittest.main()