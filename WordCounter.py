import sys
import os
import constants
from typing import List
from collections import defaultdict
from InputReader import InputReader, FileReader, CommandLineReader
from pathlib import Path
from InputCleaner import InputCleaner
from SourceLoader import SourceFromCommandLineLoader, SourceLoader

class WordCounter:
    """
    Counts the number of appearances of words within several given sources
    """

    def __init__(self, inputCleaner: InputCleaner, sourceLoader: SourceLoader):
        self.inputCleaner = inputCleaner
        self.sourceLoader = sourceLoader

    def countWords(self):
        # load the sources to read from
        sources: List[InputReader] = self.sourceLoader.loadSources()

        for source in sources:
            # read and clean the input from the source
            input = source.readInput()
            input = self.inputCleaner.cleanInput(input)

            # count the words
            wordsDict = defaultdict(int)
            for word in input.split(constants.WHITESPACE):
                if word != constants.EMPTY:
                    wordsDict[word] += 1

            # output words and appearances
            print("Word count for file '{0}'".format(source.identifier))
            for key in wordsDict:
                print("{0}: {1} time(s)".format(key, wordsDict[key]))
            print()

# try to get the location of the file configuring the words to exclude
wordsToExcludePath = ""
if len(sys.argv) == 3:
    wordsToExcludePath = sys.argv[2]

# try to get the location of the file configuring the symbols to strip
symbolsToStripPath = ""
if len(sys.argv) >= 2:
    symbolsToStripPath = sys.argv[1]

# composition root
inputCleaner: InputCleaner = InputCleaner(inputReaderType = FileReader, wordsToExcludePath = wordsToExcludePath, symbolsToStripPath = symbolsToStripPath)
sourceLoader: SourceFromCommandLineLoader = SourceFromCommandLineLoader(inputReaderType = FileReader, inputReader = CommandLineReader("file to read: "))
wordCounter: WordCounter = WordCounter(inputCleaner, sourceLoader)

# count the words
wordCounter.countWords()