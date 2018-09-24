import unittest
from unittest.mock import patch, Mock
import sys
sys.path.append('/Users/cs/Dropbox/Studium/Master/Semester 3/03_VV')
from VV_E1_WordCount.InputReader import InputReader
from VV_E1_WordCount.InputCleaner import InputCleaner


EMPTY = ""
WHITESPACE = " "
INPUT = "INPUT"
SYMBOLS = ".,;:!"
WORDS = "der, die, das,"
TEXT = "Der. das. die, wieso weshalb warum"
CLEANED_TEXT = "das wieso weshalb warum"

class InputCleanerTest(unittest.TestCase):

    @patch('VV_E1_WordCount.InputReader.InputReader.readInput', lambda x: SYMBOLS)
    def test_loadSymbolsToStrip_returnsSymbols(self):
        # arrange
        inputCleaner: InputCleaner = InputCleaner(inputReaderType = InputReader, wordsToExcludePath = INPUT, symbolsToStripPath = INPUT)
        # act
        symbols = inputCleaner.loadSymbolsToStrip(EMPTY)

        # assert
        self.assertEqual(len(symbols), 5)

    @patch('VV_E1_WordCount.InputReader.InputReader.readInput', lambda x: EMPTY)
    def test_loadSymbolsToStrip_returnsEmptyWhenNothingToRead(self):
        # arrange
        inputCleaner: InputCleaner = InputCleaner(inputReaderType = InputReader, wordsToExcludePath = INPUT, symbolsToStripPath = INPUT)
        # act
        symbols = inputCleaner.loadSymbolsToStrip(EMPTY)

        # assert
        self.assertEqual(symbols, [])

    @patch('VV_E1_WordCount.InputReader.InputReader.readInput', lambda x: WORDS)
    def test_loadWordsToExclude_returnsSymbols(self):
        # arrange
        inputCleaner: InputCleaner = InputCleaner(inputReaderType = InputReader, wordsToExcludePath = INPUT, symbolsToStripPath = INPUT)
        # act
        words = inputCleaner.loadWordsToExclude(EMPTY)

        # assert
        self.assertEqual(len(words), 3)

    @patch('VV_E1_WordCount.InputReader.InputReader.readInput', lambda x: EMPTY)
    def test_loadWordsToExclude_returnsEmptyWhenNothingToRead(self):
        # arrange
        inputCleaner: InputCleaner = InputCleaner(inputReaderType = InputReader, wordsToExcludePath = INPUT, symbolsToStripPath = INPUT)
        # act
        words = inputCleaner.loadWordsToExclude(EMPTY)

        # assert
        self.assertEqual(words, [])

    def test_cleanInputCleansInputCorrectly(self):
        # arrange
        inputCleaner: InputCleaner = InputCleaner(inputReaderType = InputReader, wordsToExcludePath = INPUT, symbolsToStripPath = INPUT)
        inputCleaner.symbolsToStrip = [',', '.']
        inputCleaner.wordsToExclude = ["der", "die"]

        # act
        text = inputCleaner.cleanInput(TEXT)

        # assert
        self.assertEqual(text.replace(WHITESPACE, EMPTY), CLEANED_TEXT.replace(WHITESPACE, EMPTY))


if __name__ == '__main__':
    unittest.main()