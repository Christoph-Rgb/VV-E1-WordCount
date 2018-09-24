import unittest
from unittest.mock import patch, Mock
import sys
sys.path.append('/Users/cs/Dropbox/Studium/Master/Semester 3/03_VV')
from VV_E1_WordCount.SourceLoader import SourceLoader, SourceFromCommandLineLoader
from VV_E1_WordCount.InputReader import InputReader

EMPTY = ""
INPUT = "INPUT"

# dummy test of the abstract class
class SourceLoaderTest(unittest.TestCase):
    def test(self):
        sourceLoader = SourceLoader()
        sourceLoader.loadSources()

class SourceFromCommandLineLoaderTest(unittest.TestCase):

    def test_returnsEmptyArrayWhenNothingIsInput(self):
        # arrange
        mock = Mock()
        mock.side_effect = [EMPTY]
        inputReader = InputReader(EMPTY)
        inputReader.readInput = mock
        sourceLoader = SourceFromCommandLineLoader(inputReaderType = InputReader, inputReader = inputReader)

        # act
        sources = sourceLoader.loadSources()

        # assert
        self.assertEqual(sources, [])

    def test_returnArrayOfLengthOneForOneInput(self):
        # arrange
        mock = Mock()
        mock.side_effect = [INPUT, EMPTY]
        inputReader = InputReader(EMPTY)
        inputReader.readInput = mock
        sourceLoader = SourceFromCommandLineLoader(inputReaderType = InputReader, inputReader = inputReader)

        # act
        sources = sourceLoader.loadSources()

        # assert
        self.assertEqual(len(sources), 1)
        self.assertEqual(type(sources[0]), InputReader)

    def test_returnArrayOfLength3ForThreeInputs(self):
        # arrange
        mock = Mock()
        mock.side_effect = [INPUT, INPUT, INPUT, EMPTY]
        inputReader = InputReader(EMPTY)
        inputReader.readInput = mock
        sourceLoader = SourceFromCommandLineLoader(inputReaderType = InputReader, inputReader = inputReader)

        # act
        sources = sourceLoader.loadSources()

        # assert
        self.assertEqual(len(sources), 3)
        for source in sources:
            self.assertEqual(type(source), InputReader)

    def test_catchesFileNotFoundAssertion(self):
        # arrange
        mock = Mock()
        mock.side_effect = [INPUT, EMPTY]
        inputReader = InputReader(EMPTY)
        inputReader.readInput = mock

        mock2 = Mock()
        mock2.side_effect = AssertionError

        sourceLoader = SourceFromCommandLineLoader(inputReaderType = mock2, inputReader = inputReader)

        # act
        sources = sourceLoader.loadSources()

        # assert
        self.assertEqual(sources, [])


if __name__ == '__main__':
    unittest.main()
