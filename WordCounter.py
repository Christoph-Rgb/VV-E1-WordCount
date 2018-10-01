import sys
import os
from typing import List
from pathlib import Path
from collections import defaultdict

sys.path.append('./')
import VV_E1_WordCount.constants as constants
from VV_E1_WordCount.InputReader import InputReader, FileReader, CommandLineReader
from VV_E1_WordCount.InputCleaner import InputCleaner
from VV_E1_WordCount.SourceLoader import SourceFromCommandLineLoader, SourceLoader
from VV_E1_WordCount.OutputWriter import OutputToConsoleWriter

#sys.path.append('/Users/cs/Dropbox/Studium/Master/Semester 3/03_VV/Exercise1')

# import VV_E1_WordCount.constants as constants
# from VV_E1_WordCount.InputReader import InputReader, FileReader, CommandLineReader
# from VV_E1_WordCount.InputCleaner import InputCleaner
# from VV_E1_WordCount.SourceLoader import SourceFromCommandLineLoader, SourceLoader
# from VV_E1_WordCount.OutputWriter import OutputToConsoleWriter

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
                if word != constants.EMPTY and word not in self.inputCleaner.wordsToExclude:
                    wordsDict[word] += 1

            wordCount[source.identifier] = wordsDict

        return wordCount