import tkinter as tk
import ctypes
import voice_assistant
from english_words import get_czech_word, get_english_word, get_random_number

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("English Cards")
        self.root.geometry("850x400")
        self.root.resizable(False, False)
        self.random_number = get_random_number()
        self.click_check = 0
        self.word_counter = 0

        self.label = self.main_label(text='Vítej! Klikni Next pro start.')
        self.motivation_label = self.motivation_label(text=self.get_motivation_text(self.word_counter))
        self.trsl_button = self.translate_button("Translate", self.get_czech_word_label)
        self.nxt_button = self.next_button("Next", self.get_english_word_label)

        self.button_state = tk.BooleanVar(value=False)
        self.voice_button = self.voice_button(self.get_voice_logo(), self.get_voice_click_on)

        #hide CMD window
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)
        
        self.root.mainloop()

    def main_label(self,text):
        label = tk.Label(self.root, text=text, font=("Helvetica",30), width=40)
        label.place(relx=0.5, rely=0.25, anchor="center")
        return label
    
    def motivation_label(self, text):
        label = tk.Label(self.root, text=text, font=("Helvetica", 20), wraplength=300, anchor="w")
        label.place(relx=0.02, rely=0.98, anchor="sw")
        return label

    def get_motivation_text(self, word_counter):
        if word_counter == 0:
            return f"Jdem na to, hodně zdaru!"
        if word_counter == 1:
            return f"Máš procvičenou {word_counter} frázi!"
        if word_counter == 2 or word_counter == 3 or word_counter == 4:
            return f"Máš procvičené {word_counter} fráze!"
        if word_counter > 4 and word_counter <= 10:
             return f"Máš procvičeno {word_counter} frází!"
        if word_counter > 10 and word_counter <= 20:
            return f"Hovno {word_counter} frází už!"
        if word_counter > 20 and word_counter <= 40:
            return f"Tak to jsi blázen už máš {word_counter} frází!"
        if word_counter > 40:
            return f"Hele brzdi už, chce to pauzu, máš {word_counter} frází!"

    def translate_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 20), width=10, height=1)
        button.place(relx=0.4, rely=0.6, anchor="center")
        return button
    
    def next_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 20), width=10, height=1)
        button.place(relx=0.62, rely=0.6, anchor="center")
        return button
    
    def voice_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 15), width=4, height=2)
        button.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)
        return button

    def get_czech_word_label(self):
        self.click_check += 1
        if self.click_check == 1:
            self.label.config(text=get_czech_word(self.random_number))
            self.random_number = get_random_number()
            self.word_counter += 1
            self.motivation_label.config(text=self.get_motivation_text(self.word_counter))

    def get_english_word_label(self):
        self.label.config(text=get_english_word(self.random_number))
        self.click_check = 0
        

    def get_voice_logo(self):
        return "🔊"

    def get_voice_click_on(self):
        voice_assistant.VoiceAssistant(get_english_word(self.random_number))
