import unittest
from unittest.mock import patch, Mock
import sys

sys.path.append('../')
from VV_E1_WordCount.SourceLoader import SourceLoader, SourceFromCommandLineLoader
from VV_E1_WordCount.InputReader import InputReader

EMPTY = ""
INPUT = "INPUT"

# dummy test of the abstract class
class SourceLoaderTest(unittest.TestCase):
    def test(self):
        sourceLoader = SourceLoader()
        sourceLoader.loadSources()

# tests for SourceFromCommandLineLoader
class SourceFromCommandLineLoaderTest(unittest.TestCase):

    def test_loadSources_returnsEmptyArrayWhenNothingIsInput(self):
        # arrange
        readInputMock = Mock()
        readInputMock.return_value = EMPTY
        inputReader = InputReader(EMPTY)
        inputReader.readInput = readInputMock
        sourceLoader = SourceFromCommandLineLoader(inputReaderType = InputReader, inputReader = inputReader)

        # act
        sources = sourceLoader.loadSources()

        # assert
        self.assertEqual(sources, [])

    def test_loadSources_returnsArrayOfLengthOneForOneInput(self):
        # arrange
        readInputMock = Mock()
        readInputMock.side_effect = [INPUT, EMPTY]
        inputReader = InputReader(EMPTY)
        inputReader.readInput = readInputMock
        sourceLoader = SourceFromCommandLineLoader(inputReaderType = InputReader, inputReader = inputReader)

        # act
        sources = sourceLoader.loadSources()

        # assert
        self.assertEqual(len(sources), 1)
        self.assertEqual(type(sources[0]), InputReader)

    def test_loadSources_returnsArrayOfLength3ForThreeInputs(self):
        # arrange
        readInputMock = Mock()
        readInputMock.side_effect = [INPUT, INPUT, INPUT, EMPTY]
        inputReader = InputReader(EMPTY)
        inputReader.readInput = readInputMock
        sourceLoader = SourceFromCommandLineLoader(inputReaderType = InputReader, inputReader = inputReader)

        # act
        sources = sourceLoader.loadSources()

        # assert
        self.assertEqual(len(sources), 3)
        for source in sources:
            self.assertEqual(type(source), InputReader)

    def test_loadSources_returnsEmptyListForFileNotFoundAssertion(self):
        # arrange
        readInputMock = Mock()
        readInputMock.side_effect = [INPUT, EMPTY]
        inputReader = InputReader(EMPTY)
        inputReader.readInput = readInputMock

        assertionErrorInputReaderMock = Mock()
        assertionErrorInputReaderMock.side_effect = AssertionError

        sourceLoader = SourceFromCommandLineLoader(inputReaderType = assertionErrorInputReaderMock, inputReader = inputReader)

        # act
        sources = sourceLoader.loadSources()

        # assert
        self.assertEqual(sources, [])


if __name__ == '__main__':
    unittest.main()
