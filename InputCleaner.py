import sys
sys.path.append('/Users/cs/Dropbox/Studium/Master/Semester 3/03_VV')

import os
import VV_E1_WordCount.constants as constants
from typing import List, TypeVar, Generic
from VV_E1_WordCount.InputReader import InputReader

# generic variable for the input reader
T = TypeVar('T')

class InputCleaner:
    """
    Cleans the input by removing line breaks, removing words that are to be excluded and symbols that are to be stripped
    """

    def __init__(self, inputReaderType: T, wordsToExcludePath: str, symbolsToStripPath: str):
        self.inputReaderType = inputReaderType
        self.wordsToExclude: List[str] = self.loadWordsToExclude(wordsToExcludePath)
        self.symbolsToStrip: List[str] = self.loadSymbolsToStrip(symbolsToStripPath)

    def cleanInput(self, input: str):

        # cast to lower case
        input = input.lower()

        # replace line breaks by whitespace
        input = input.replace(os.linesep, constants.WHITESPACE)

        # replace symbols to be excluded by whitespace
        for symbol in self.symbolsToStrip:
            input = input.replace(symbol, constants.WHITESPACE)

        # replace words to be excluded by whitespace
        for word in self.wordsToExclude:
            input = input.replace(word, constants.WHITESPACE)

        return input

    def loadWordsToExclude(self, wordsToExcludePath: str):
        wordsToExclude: List[str] = []

        # try to load words that are to be excluded
        try:
            wordsToExcludeInputReader = self.inputReaderType(wordsToExcludePath)
            words = wordsToExcludeInputReader.readInput()
            words = words.lower()
            words = words.replace(constants.WHITESPACE, constants.EMPTY)
            splittedWords = words.split(constants.COMMA)
            splittedWords.remove("")
            wordsToExclude.extend(splittedWords)
        
        finally:
            return wordsToExclude

    def loadSymbolsToStrip(self, symbolsToStripPath: str):
        symbolsToStrip: List[str] = []

        # try to load symbols that are to be stripped from the input 
        try:
            symbolsToStripInputReader = self.inputReaderType(symbolsToStripPath)
            symbols = symbolsToStripInputReader.readInput()
            for symbol in symbols:
                symbolsToStrip.append(symbol)
        finally:
            return symbolsToStrip
