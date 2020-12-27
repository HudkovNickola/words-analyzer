#Application
An application that allows you to recognize the word that is said in sentences.
In this example, the application recognizes a mouse and a computer mouse.

For a more precise definition of the word, you can find a more accurate text for training objects.
1. Path to text to train the mouse object: /static/alive/en.wikipedia.org.wiki.Computer_mouse.txt
2. Path to text to train the computer-mouse object: /static/not_alive/en.wikipedia.org.wiki.Mouse.txt

Text file for sentence analysis:  /static/analyze/text.txt

Application launch:
$PYTHONPATH/python main.py

#TODO
1. Add the word search algorithm, in case the repetitions of words in the text for training.
   This will increase the chance of correct answer.
   
2. Add tests.
