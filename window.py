import tkinter as tk
import ctypes
from english_words import ENGLISH_WORD

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("English Cards")
        self.root.geometry("800x600")

        self.label = self.main_label(ENGLISH_WORD)

        #hide CMD window
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)
        
        self.root.mainloop()

    def main_label(self,text):
        label = tk.Label(self.root, text=text)
        label.pack(pady=20)
        return label


    def main_button(self):
        pass