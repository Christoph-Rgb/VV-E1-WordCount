import sys
from typing import List, TypeVar, Generic

sys.path.append('./')
import VV_E1_WordCount.constants as constants
from VV_E1_WordCount.InputReader import InputReader

# generic variable for the input reader
T = TypeVar('T')

class SourceLoader(Generic[T]):
    def loadSources(self):
        pass

class SourceFromCommandLineLoader(Generic[T], SourceLoader):
    """
    Loads the sources that are to be read from the command line
    """

    def __init__(self, inputReaderType: T, inputReader: InputReader):
        self.inputReader = inputReader
        self.sourceType = inputReaderType

    def loadSources(self):
        """
        Loads sources that are to be read from the command line (line by line)
        """

        sources: List[self.sourceType] = []

        #read sources until nothing is input
        sourcePath = self.inputReader.readInput()
        while (sourcePath != constants.EMPTY):

            # create reader for the source and append it to the list of sources
            try:
                sourceReader = self.sourceType(sourcePath)
                sources.append(sourceReader)
            except AssertionError:
                print("source does not exist")

            # ask for another source
            sourcePath = self.inputReader.readInput()

        return sources