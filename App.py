import sys
sys.path.append('../')

from VV_E1_WordCount.InputReader import InputReader, FileReader, CommandLineReader
from VV_E1_WordCount.InputCleaner import InputCleaner
from VV_E1_WordCount.SourceLoader import SourceFromCommandLineLoader, SourceLoader
from VV_E1_WordCount.OutputWriter import OutputToConsoleWriter
from VV_E1_WordCount.WordCounter import WordCounter
import VV_E1_WordCount.constants as constants

# try to get the location of the file configuring the words to exclude
wordsToExcludePath = ""
wordsToExcludeInputReader = None
if len(sys.argv) == 3:
    wordsToExcludePath = sys.argv[2]
try:
    wordsToExcludeInputReader = FileReader(wordsToExcludePath)
    #wordsToExcludeInputReader = FileReader("./config/words_to_exclude.csv")
except(AssertionError):
    wordsToExcludeInputReader = InputReader(constants.EMPTY)


# try to get the location of the file configuring the symbols to strip
symbolsToStripPath = ""
symbolsToStripInputReader = None
if len(sys.argv) >= 2:
    symbolsToStripPath = sys.argv[1]
try:
    symbolsToStripInputReader = FileReader(symbolsToStripPath)
    #symbolsToStripInputReader = FileReader("./config/symbols_to_strip")
except(AssertionError):
    symbolsToStripInputReader = InputReader(constants.EMPTY)

# composition root
inputCleaner: InputCleaner = InputCleaner(wordsToExcludeInputReader, symbolsToStripInputReader)
sourceLoader: SourceFromCommandLineLoader = SourceFromCommandLineLoader(inputReaderType = FileReader, inputReader = CommandLineReader("file to read: "))
wordCounter: WordCounter = WordCounter(inputCleaner, sourceLoader)

# count the words
wordCount = wordCounter.countWords()

# wirte output to console
outputWriter = OutputToConsoleWriter()
outputWriter.printOutput(wordCount)