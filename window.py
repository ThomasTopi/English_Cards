import tkinter as tk
import ctypes
from english_words import ENGLISH_WORD

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("English Cards")
        self.root.geometry("600x400")

        self.label = self.main_label(ENGLISH_WORD)
        self.button = self.main_button("Next Word", self.get_word)

        self.button_state = tk.BooleanVar(value=False)
        self.voice_button = self.voice_button(self.get_voice_logo(), self.get_voice_click_on)

        #hide CMD window
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)
        
        self.root.mainloop()

    def main_label(self,text):
        label = tk.Label(self.root, text=text, font=("Helvetica",30), width=40)
        label.pack(pady=50)
        return label

    def main_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 20), width=10, height=5)
        button.pack(pady=60)
        return button
    
    def voice_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 15), width=5, height=5)
        button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        return button

    def get_word(self):
        self.label.config(text="next word")

    def get_voice_logo(self):
        if self.button_state.get():
            return "🔊"
        else:
            return "🔇"

    def get_voice_click_on(self):
        current_state = self.button_state.get()
        #Prepne state na False
        self.button_state.set(not current_state)
        #nastaveni loga na button voice_button
        self.voice_button.config(text=self.get_voice_logo())
