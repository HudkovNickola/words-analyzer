from functools import wraps

from nltk import pos_tag, download, word_tokenize
from nltk.stem import WordNetLemmatizer

from app.object.state_word import StateObject

libs = ('punkt', 'wordnet', 'averaged_perceptron_tagger', 'universal_tagset')
[download(lib) for lib in libs]
support_pos = ["VERB", "ADJ", "NOUN"]


def _read_file_per_line(function):
    """
    The decorator for reading file per line
    :param function: for wrapping
    :return: wrapper
    """
    @wraps(function)
    def wrapper(self, *args):
        with open(self.path_to_file) as file:
            for index, line in enumerate(file):
                function(self, index, line, *args)

    return wrapper


class FileService:
    """
    File service for reading files
    """
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    @staticmethod
    def filteringSupportWords(line):
        """
        Method for the filtering words by POS, support only VERB, ADJ, NOUN pos.
        :parameter line with words
        """

        def getPOS(entry):
            return entry[1]

        word_pos = pos_tag(word_tokenize(line), tagset='universal')
        return list(filter(lambda entry: getPOS(entry) in support_pos, word_pos))

    @_read_file_per_line
    def actionPerLine(self, index, line, function):
        """
        Method for performing any actions on lines from a file
        :parameter index line
        :parameter line with words
        :parameter function action on line
        """
        function(self.filteringSupportWords(line), line, index)


class FileTeacher(FileService):
    """
    Class for teaching objects to words from files
    """
    lemmatizer = WordNetLemmatizer()

    def __init__(self, path_to_file):
        super().__init__(path_to_file)

    @_read_file_per_line
    def readFileAndTeachObject(self, index, line, baseObject: StateObject):
        """
        Reading words from a file and teaching an object
        :parameter index line
        :parameter line with words
        :parameter baseObject object for teaching words from line
        """
        new_dict = dict()
        self.distributeByType(line, new_dict)
        baseObject.mergeWords(new_dict)

    def distributeByType(self, line, new_dict):
        for word, tpe in self.filteringSupportWords(line):
            word = FileTeacher.lemmatizer.lemmatize(word.lower())
            if type(new_dict.get(tpe)) is set:
                new_dict[tpe].update({word})
            else:
                new_dict[tpe] = {word}
