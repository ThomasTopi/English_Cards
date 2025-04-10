import tkinter as tk
import ctypes
from english_words import get_czech_word, get_english_word, get_random_number

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("English Cards")
        self.root.geometry("800x200")
        self.root.resizable(False, False)
        self.random_number = get_random_number()
        self.click_check = 0

        self.label = self.main_label(text='Vítej! Klikni Next pro start.')
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

    def get_english_word_label(self):
        self.label.config(text=get_english_word(self.random_number))
        self.click_check = 0
        

    def get_voice_logo(self):
        # if self.button_state.get():
        #     return "🔊"
        # else:
        #     return "🔇"
        return "🔊"

    def get_voice_click_on(self):
        current_state = self.button_state.get()
        #Prepne state na False
        self.button_state.set(not current_state)
        #nastaveni loga na button voice_button
        self.voice_button.config(text=self.get_voice_logo())
