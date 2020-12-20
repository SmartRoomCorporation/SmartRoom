import tkinter as tk
import json

class Gui:
    window = tk.Tk()
    window.geometry("600x600")
    window.title("SmartRoom")
    sr = ""
    text_output = ""
    count = 0

    def run(self):
        self.initGui()
        self.refreshMeasure()
        self.window.mainloop()

    def initGui(self):
        s_button = tk.Button(text="Click 2", command=self.ciaone)
        s_button.grid(row=2, column=0,sticky="W")

    def callSr(self):
        self.text_output = tk.Label(self.window, text=json.dumps(self.sr.getRoomStatus()), fg="green", font=("Helevetica", 16))
        self.text_output.grid(row=1, column=1, padx=50, sticky="W")

    def refreshMeasure(self):
        self.callSr()
        self.window.after(1000, self.refreshMeasure)

    def ciaone(self):
        self.count = self.count + 1
        self.text_output = tk.Label(self.window, text="Strunz" + str(self.count), fg="green", font=("Helevetica", 16))
        self.text_output.grid(row=3, column=1, padx=50, sticky="W")

    def setRoom(self, sr):
        self.sr = sr