from re import sub
from functools import reduce

from app.service.file_service import FileService

MESSAGE_NOT_UNDERSTAND = "No way to define. Teach objects better."


class Analyzer:
    """
    Analyzer service for analyze the words in lines from source file, to understand what the sentences are about
    """

    def __init__(self, file_with_text, states):
        self.sourceText = FileService(file_with_text)
        self.states = states
        self.result = dict()

    def analyze(self):
        """
        Analyze sentences to understand where more word matches were found
        """
        self.sourceText.actionPerLine(lambda text, line, index: self.buildResponse(index, line, text))

    def buildResponse(self, index, line, text):
        """
        Build of a complete report with analyzed data
        """
        line = sub("\n", "", line)
        self.result[index] = {"line": line, "details": [{state.getKeyWord(): state.countingOccurrencesWordsFromLine(text)} for state in self.states]}

    def qualifyAndPrintResult(self):
        """
        Qualify what the sentence says and displays the result
        """
        for entry in self.result:
            details_ = self.result[entry]["details"]
            self.printResult(self.qualifyKeyWord(details_), self.result.get(entry)["line"])

    @staticmethod
    def qualifyKeyWord(details_):
        def getCounter(detail):
            return list(detail.values())[0]

        def getKey(detail):
            return list(detail.keys())[0]

        return reduce(lambda current, nextObject:
                      getKey(current)
                      if getCounter(current) > getCounter(nextObject)
                      else MESSAGE_NOT_UNDERSTAND
                      if getCounter(current) == getCounter(nextObject)
                      else getKey(nextObject),
                      details_)

    @staticmethod
    def printResult(keyWord, line):
        print(f'Analyzed sentence ===> {line}')
        print(f'It is ===> {keyWord}', end='\n\n')
