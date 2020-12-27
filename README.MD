###### **Application**

An application that allows you to recognize the word that is said in sentences.
In this example, the application recognizes a mouse and a computer mouse.

For a more precise definition of the word, you can find a more accurate text for training objects.
1. Path to text to train the mouse object: _/static/alive/en.wikipedia.org.wiki.Computer_mouse.txt_
2. Path to text to train the computer-mouse object: _/static/not_alive/en.wikipedia.org.wiki.Mouse.txt_

Text file for sentence analysis:  _/static/analyze/text.txt_

Application launch:

_$PYTHONPATH/python main.py_

###### **TODO**
1. Add the word search algorithm, in case the repetitions of words in the text for training.
   This will increase the chance of correct answer.
   
2. Add tests.
