import unittest
from unittest.mock import patch, Mock
import sys

sys.path.append('../')
from VV_E1_WordCount.InputReader import InputReader
from VV_E1_WordCount.InputCleaner import InputCleaner


EMPTY = ""
WHITESPACE = " "
INPUT = "INPUT"
SYMBOLS = ".,;:!"
WORDS = "der, die, das,"
TEXT = "Der. das. die, wieso ! weshalb..warum \n"
CLEANED_TEXT = "der das die wieso weshalb warum"

class InputCleanerTest(unittest.TestCase):

    # helper method raising an error
    def raiseValueError(self):
        raise(ValueError("test"))

    def test_loadSymbolsToStrip_returnsSymbols(self):
        # arrange
        readSymbolsMock = Mock()
        readSymbolsMock.return_value = SYMBOLS
        symbolsReader = InputReader(EMPTY)
        symbolsReader.readInput = readSymbolsMock

        wordReaderMock = Mock()
        wordReaderMock.return_value = EMPTY
        wordsReader = InputReader(EMPTY)
        wordsReader.readInput = wordReaderMock

        # act
        inputCleaner: InputCleaner = InputCleaner(wordsReader, symbolsReader)
        symbols = inputCleaner.symbolsToStrip

        # assert
        self.assertEqual(len(symbols), 5)
        self.assertEqual(symbols, [".", ",", ";", ":", "!"])

    def test_loadSymbolsToStrip_returnsEmptyWhenNothingToRead(self):
        # arrange
        readSymbolsMock = Mock()
        readSymbolsMock.return_value = EMPTY
        symbolsReader = InputReader(EMPTY)
        symbolsReader.readInput = readSymbolsMock

        wordReaderMock = Mock()
        wordReaderMock.return_value = EMPTY
        wordsReader = InputReader(EMPTY)
        wordsReader.readInput = wordReaderMock

        # act
        inputCleaner: InputCleaner = InputCleaner(wordsReader, symbolsReader)
        symbols = inputCleaner.symbolsToStrip

        # assert
        self.assertEqual(symbols, [])

    def test_loadSymbolsToStrip_returnsEmptyWhenErrorOccurs(self):
        # arrange
        readSymbolsMock = Mock()
        readSymbolsMock.side_effect = [AssertionError]
        symbolsReader = InputReader(EMPTY)
        symbolsReader.readInput = readSymbolsMock

        wordReaderMock = Mock()
        wordReaderMock.return_value = EMPTY
        wordsReader = InputReader(EMPTY)
        wordsReader.readInput = wordReaderMock

        # act
        inputCleaner: InputCleaner = InputCleaner(wordsReader, symbolsReader)
        symbols = inputCleaner.symbolsToStrip

        # assert
        self.assertEqual(symbols, [])

    def test_loadWordsToExclude_returnsWords(self):
        # arrange
        symbolsReader = InputReader(EMPTY)
        symbolsReaderMock = Mock()
        symbolsReader.return_value = EMPTY
        symbolsReader.readInput = symbolsReaderMock

        wordsReader = InputReader(EMPTY)
        wordsReaderMock = Mock()
        wordsReaderMock.return_value = WORDS
        wordsReader.readInput = wordsReaderMock
        
        # act
        inputCleaner: InputCleaner = InputCleaner(wordsReader, symbolsReader)
        words = inputCleaner.wordsToExclude

        # assert
        self.assertEqual(len(words), 3)
        self.assertEqual(words, ["der", "die", "das"])

    def test_loadWordsToExclude_returnsEmptyWhenNothingToRead(self):
        # arrange
        symbolsReader = InputReader(EMPTY)
        symbolsReaderMock = Mock()
        symbolsReader.return_value = EMPTY
        symbolsReader.readInput = symbolsReaderMock

        wordsReader = InputReader(EMPTY)
        wordsReaderMock = Mock()
        wordsReaderMock.return_value = EMPTY
        wordsReader.readInput = wordsReaderMock
        
        # act
        inputCleaner: InputCleaner = InputCleaner(wordsReader, symbolsReader)
        words = inputCleaner.wordsToExclude

        # assert
        self.assertEqual(words, [])

    def test_loadWordsToExclude_returnsEmptyOnError(self):
        # arrange
        symbolsReader = InputReader(EMPTY)
        symbolsReaderMock = Mock()
        symbolsReader.return_value = EMPTY
        symbolsReader.readInput = symbolsReaderMock

        wordsReader = InputReader(EMPTY)
        wordsReaderMock = Mock()
        wordsReaderMock.side_effect = [AssertionError]
        wordsReader.readInput = wordsReaderMock
        
        # act
        inputCleaner: InputCleaner = InputCleaner(wordsReader, symbolsReader)
        words = inputCleaner.wordsToExclude

        # assert
        self.assertEqual(words, [])

    def test_cleanInputCleansInputCorrectly(self):
        # arrange
        symbolsReader = InputReader(EMPTY)
        wordsReader = InputReader(EMPTY)
        inputCleaner: InputCleaner = InputCleaner(wordsReader, symbolsReader)

        inputCleaner.symbolsToStrip = [',', '.', '!']
        inputCleaner.wordsToExclude = ["der", "die"]

        # act
        text = inputCleaner.cleanInput(TEXT)

        # assert
        self.assertEqual(text.replace(WHITESPACE, EMPTY), CLEANED_TEXT.replace(WHITESPACE, EMPTY))


if __name__ == '__main__':
    unittest.main()
