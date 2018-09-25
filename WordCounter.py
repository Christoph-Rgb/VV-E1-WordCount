import sys
sys.path.append('/Users/cs/Dropbox/Studium/Master/Semester 3/03_VV')

import os
import VV_E1_WordCount.constants as constants
from typing import List
from collections import defaultdict
from VV_E1_WordCount.InputReader import InputReader, FileReader, CommandLineReader
from pathlib import Path
from VV_E1_WordCount.InputCleaner import InputCleaner
from VV_E1_WordCount.SourceLoader import SourceFromCommandLineLoader, SourceLoader
from VV_E1_WordCount.OutputWriter import OutputToConsoleWriter

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

        # store for the word count for every source that was read
        wordCount = {}

        for source in sources:
            # read and clean the input from the source
            input = source.readInput()
            input = self.inputCleaner.cleanInput(input)

            # count the words
            wordsDict = defaultdict(int)
            for word in input.split(constants.WHITESPACE):
                if word != constants.EMPTY:
                    wordsDict[word] += 1

            wordCount[source.identifier] = wordsDict

        return wordCount

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
wordCount = wordCounter.countWords()

# wirte output to console
outputWriter = OutputToConsoleWriter()
outputWriter.printOutput(wordCount)