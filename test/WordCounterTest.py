import unittest
from unittest.mock import patch, Mock
import sys
from collections import defaultdict
import io

sys.path.append('../')
from VV_E1_WordCount.SourceLoader import SourceLoader, SourceFromCommandLineLoader
from VV_E1_WordCount.InputReader import InputReader
from VV_E1_WordCount.WordCounter import WordCounter
from VV_E1_WordCount.InputCleaner import InputCleaner

WORDS_TO_EXCLUDE = "das, bou"

EMPTY = ""
INPUT = "INPUT"
FILE = "file.file"
TEXT = "der die das der die das der der der"
OUTPUT = {}
OUTPUT[FILE] = defaultdict(int)
OUTPUT[FILE]["der"] = 5
OUTPUT[FILE]["die"] = 2

FILE2 = "file2.file"
TEXT2 = "a bou mou dou wos a bou dou mou"
OUTPUT2 = {}

OUTPUT2[FILE] = defaultdict(int)
OUTPUT2[FILE]["der"] = 5
OUTPUT2[FILE]["die"] = 2

OUTPUT2[FILE2] = defaultdict(int)
OUTPUT2[FILE2]["a"] = 2
OUTPUT2[FILE2]["mou"] = 2
OUTPUT2[FILE2]["dou"] = 2
OUTPUT2[FILE2]["wos"] = 1


class WordCounterTest(unittest.TestCase):

    def test_countWords_countsCorrectlyForNoFile(self):
        # assert
        sourceLoader = SourceLoader()
        sourceLoaderMock = Mock()
        sourceLoaderMock.return_value = []
        sourceLoader.loadSources = sourceLoaderMock

        inputCleaner = InputCleaner(InputReader(EMPTY), InputReader(EMPTY))
        wordCounter = WordCounter(inputCleaner, sourceLoader)

        # act
        output = wordCounter.countWords()

        # assert
        self.assertEqual(output, {})

    def test_countWords_countsCorrectlyForEmptyFile(self):
        # arrange
        inputReader = InputReader(FILE)
        inputReaderMock = Mock()
        inputReaderMock.return_value = EMPTY
        inputReader.readInput = inputReaderMock

        sourceLoader = SourceLoader()
        sourceLoaderMock = Mock()
        sourceLoaderMock.side_effect = [[inputReader]]
        sourceLoader.loadSources = sourceLoaderMock

        inputCleaner = InputCleaner(InputReader(EMPTY), InputReader(EMPTY))

        wordCounter = WordCounter(inputCleaner, sourceLoader)

        # act
        output = wordCounter.countWords()

        # assert
        expected = {}
        expected[FILE] = defaultdict(int)
        self.assertEqual(output, expected)

    def test_countWords_countsCorrectlyForOneFile(self):
        # arrange
        inputReader = InputReader(FILE)
        inputReaderMock = Mock()
        inputReaderMock.return_value = TEXT
        inputReader.readInput = inputReaderMock

        sourceLoader = SourceLoader()
        sourceLoaderMock = Mock()
        sourceLoaderMock.return_value = [inputReader]
        sourceLoader.loadSources = sourceLoaderMock

        wordsToExcludeInputReader = InputReader(EMPTY)
        wordsToExcludeInputReaderMock = Mock()
        wordsToExcludeInputReaderMock.return_value = WORDS_TO_EXCLUDE
        wordsToExcludeInputReader.readInput = wordsToExcludeInputReaderMock

        inputCleaner = InputCleaner(wordsToExcludeInputReader, InputReader(EMPTY))

        wordCounter = WordCounter(inputCleaner, sourceLoader)

        # act
        output = wordCounter.countWords()

        # assert
        self.assertEqual(output, OUTPUT)
    
    def test_countWords_countsCorrectlyForTwoFiles(self):
        # arrange
        inputReader = InputReader(FILE)
        inputReaderMock = Mock()
        inputReaderMock.return_value = TEXT
        inputReader.readInput = inputReaderMock

        inputReader2 = InputReader(FILE2)
        inputReaderMock2 = Mock()
        inputReaderMock2.return_value = TEXT2
        inputReader2.readInput = inputReaderMock2

        sourceLoader = SourceLoader()
        sourceLoaderMock = Mock()
        sourceLoaderMock.return_value = [inputReader, inputReader2]
        sourceLoader.loadSources = sourceLoaderMock

        wordsToExcludeInputReader = InputReader(EMPTY)
        wordsToExcludeInputReaderMock = Mock()
        wordsToExcludeInputReaderMock.return_value = WORDS_TO_EXCLUDE
        wordsToExcludeInputReader.readInput = wordsToExcludeInputReaderMock

        inputCleaner = InputCleaner(wordsToExcludeInputReader, InputReader(EMPTY))

        wordCounter = WordCounter(inputCleaner, sourceLoader)

        # act
        output = wordCounter.countWords()

        # assert
        self.assertEqual(output, OUTPUT2)

if __name__ == '__main__':
    unittest.main()
