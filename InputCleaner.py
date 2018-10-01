import sys
import os
from typing import List, TypeVar, Generic
#sys.path.append('/Users/cs/Dropbox/Studium/Master/Semester 3/03_VV/Exercise1')

sys.path.append('./')
from VV_E1_WordCount.InputReader import InputReader
import VV_E1_WordCount.constants as constants

# import VV_E1_WordCount.constants as constants
# from VV_E1_WordCount.InputReader import InputReader

class InputCleaner:
    """
    Cleans the input by removing line breaks, removing words that are to be excluded and symbols that are to be stripped
    """

    def __init__(self, wordsToExcludeInputReader: InputReader, symbolsToStripInputReader: InputReader):
        self.wordsToExclude: List[str] = self.loadWordsToExclude(wordsToExcludeInputReader)
        self.symbolsToStrip: List[str] = self.loadSymbolsToStrip(symbolsToStripInputReader)

    def cleanInput(self, input: str):

        # cast to lower case
        input = input.lower()

        # replace line breaks by whitespace
        input = input.replace(os.linesep, constants.WHITESPACE)

        # replace symbols to be excluded by whitespace
        for symbol in self.symbolsToStrip:
            input = input.replace(symbol, constants.WHITESPACE)

        return input

    def loadWordsToExclude(self, wordsToExcludeInputReader: InputReader):
        wordsToExclude: List[str] = []

        # try to load words that are to be excluded
        try:
            words = wordsToExcludeInputReader.readInput()
            words = words.lower()
            words = words.replace(constants.WHITESPACE, constants.EMPTY)
            splittedWords = words.split(constants.COMMA)
            if constants.EMPTY in splittedWords:
                splittedWords.remove(constants.EMPTY)
            wordsToExclude.extend(splittedWords)
        
        finally:
            return wordsToExclude

    def loadSymbolsToStrip(self, symbolsToStripInputReader: InputReader):
        symbolsToStrip: List[str] = []

        # try to load symbols that are to be stripped from the input 
        try:
            symbols = symbolsToStripInputReader.readInput()
            for symbol in symbols:
                if symbol != constants.EMPTY:
                    symbolsToStrip.append(symbol)
        finally:
            return symbolsToStrip