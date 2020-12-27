from nltk import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


class StateObject:
    """
    The object for teaching words
    """
    def __init__(self, keyWord):
        self.keyWord = keyWord
        self.baseState = {"NOUN": set(), "VERB": set(), "ADJ": set()}

    def mergeWords(self, states):
        """
        Merge words between current state and incoming state
        """
        for state in states:
            self.baseState[state] |= states.get(state)

    def getState(self, pos: str):
        """
        Return all words, which object studied
        """
        return self.baseState.get(pos)

    def getKeyWord(self):
        """
        The key word with which this object is associated
        """
        return self.keyWord

    def countingOccurrencesWordsFromLine(self, sourceLines):
        """
        Counting occurrences words from source line in base state words of object
        :param sourceLines: words for analyze
        :return: counter occurrences
        """
        counter = 0
        for (word, pos) in sourceLines:
            word = lemmatizer.lemmatize(word.lower())
            if word in self.baseState.get(pos):
                counter += 1
        return counter
