from glob import glob

from app.service.analyzer_service import Analyzer
from app.service.file_service import FileTeacher
from app.object.state_word import StateObject

objects = {StateObject("animal"): glob("static/alive/*.txt"),
           StateObject("computer-mouse"): glob("static/not_alive/*.txt")}

file_with_text = "static/analyze/text.txt"


def teachObject(state: StateObject, files: list):
    teachers = [FileTeacher(fileName) for fileName in files]
    [teach.readFileAndTeachObject(state) for teach in teachers]


if __name__ == "__main__":
    [teachObject(state, files) for (state, files) in objects.items()]
    states = [state for state, files in objects.items()]
    analyzer = Analyzer(file_with_text, states)
    analyzer.analyze()
    analyzer.qualifyAndPrintResult()
