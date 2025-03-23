import pyttsx3 

engine = pyttsx3.init()

text_cz = ["mám tě rád boreče"]
#text_eng = ["Homophobic"]
text_eng = [input()]

#nastaveni jazyka mluvy
voices = engine.getProperty('voices')

#check jestli je language ve windows, if so, nastavi jej jako hlas. POZOR, musi byt nainstalovany v OS.
for voice in voices:
    if 'english' in voice.id.lower():  #if 'czech' in voice.id.lower():
        engine.setProperty('voice', voice.id)

#set speed of speech
engine.setProperty('rate', 100)
#convert text to speech
engine.say(text_eng)
#speek
engine.runAndWait()