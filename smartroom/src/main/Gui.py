from threading import Thread
import tkinter as tk

class Gui(Thread):
    
    sr = ""

    def run(self):
        self.initGui()
        self.window.mainloop()

    def initGui(self):
        first_button = tk.Button(text="Click 1", command=self.callSr)

    def callSr(self):
        self.sr.pubToServ()

    def setRoom(self, sr):
        self.sr = sr