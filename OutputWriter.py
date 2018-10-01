class OutputWriter:
    def printOutput(self, output):
        pass

class OutputToConsoleWriter(OutputWriter):
    """
    Prints the output to the console
    """
    def printOutput(self, output):
        """
        Prints the output to the console
        """
        for sourceKey in output:
            sourceWordDict = output[sourceKey]

            # output words and appearances
            print("Word count for file '{0}'".format(sourceKey))
            for key in sourceWordDict:
                print("{0}: {1} time(s)".format(key, sourceWordDict[key]))
            print()
            

