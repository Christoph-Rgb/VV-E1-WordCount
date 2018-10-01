import sys
import os
from typing import List, TypeVar, Generic

sys.path.append('./')
from VV_E1_WordCount.InputReader import InputReader
import VV_E1_WordCount.constants as constants

class InputCleaner:
    """
    Cleans the input by removing line breaks and removing symbols that are to be exluded
    """

    def __init__(self, wordsToExcludeInputReader: InputReader, symbolsToStripInputReader: InputReader):
        self.wordsToExclude: List[str] = self.loadWordsToExclude(wordsToExcludeInputReader)
        self.symbolsToStrip: List[str] = self.loadSymbolsToStrip(symbolsToStripInputReader)

    def cleanInput(self, input: str):
        """
        Cleans the input by removing line breaks and removing symbols that are to be exluded
        """

        # cast to lower case
        input = input.lower()

        # replace line breaks by whitespace
        input = input.replace(os.linesep, constants.WHITESPACE)

        # replace symbols to be excluded by whitespace
        for symbol in self.symbolsToStrip:
            input = input.replace(symbol, constants.WHITESPACE)

        return input

    def loadWordsToExclude(self, wordsToExcludeInputReader: InputReader):
        """
        Returns the words that are to be excluded (provided InputReader is expected to read comma separated values - csv)
        """
        wordsToExclude: List[str] = []

        # try to load words that are to be excluded
        try:
            # read the words
            words = wordsToExcludeInputReader.readInput()
            # cast to lower case
            words = words.lower()
            # remove whitespaces
            words = words.replace(constants.WHITESPACE, constants.EMPTY)
            # split the words by comma
            splittedWords = words.split(constants.COMMA)
            # remove the empty symbol
            if constants.EMPTY in splittedWords:
                splittedWords.remove(constants.EMPTY)
            # add the words to the words to be excluded
            wordsToExclude.extend(splittedWords)
        
        finally:
            return wordsToExclude

    def loadSymbolsToStrip(self, symbolsToStripInputReader: InputReader):
        """
        Retruns the symbols that are to be stripped (provided InputReader is expected to read only symbols)
        """
        symbolsToStrip: List[str] = []

        # try to load symbols that are to be stripped from the input 
        try:
            # read the symbols
            symbols = symbolsToStripInputReader.readInput()
            # add every symbol to the list of symbols to strip if it is not the empty symbol
            for symbol in symbols:
                if symbol != constants.EMPTY:
                    symbolsToStrip.append(symbol)
        finally:
            return symbolsToStrip