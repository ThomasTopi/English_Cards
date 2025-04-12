import pyttsx3 

class VoiceAssistant:

    def __init__(self, word):
        self.word = word
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.say(self.word)
        self.engine.runAndWait()