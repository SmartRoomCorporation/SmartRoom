import tkinter as tk
import json

class Gui:
    window = tk.Tk()
    window.geometry("1200x600")
    window.title("SmartRoom")
    sr = ""
    text_output = ""
    count = 0

    def run(self):
        self.initGui()
        self.refreshMeasure()
        self.refreshCamera()
        self.window.mainloop()

    def initGui(self):
        s_button = tk.Button(text="Click 2", command=self.ciaone)
        s_button.grid(row=4, column=0,sticky="W")                    

    def callSr(self):
        self.text_output = tk.Label(self.window, text=json.dumps(self.sr.getRoomStatus()), fg="green", font=("Helevetica", 16))
        self.text_output.grid(row=1, column=1, padx=50, sticky="W")

    def refreshMeasure(self):
        self.callSr()
        self.window.after(1000, self.refreshMeasure)
    
    def refreshCamera(self):
        self.showCamera()
        self.sr.getCamera().showFaceRecon()
        self.window.after(int(1000/30), self.refreshCamera)

    def showCamera(self):
        photo = self.sr.getCamera().getCameraSimpleStream()
        self.label = tk.Label(self.window, image = photo, width=440, height=300)
        self.label.image = photo
        self.label.grid(row=2)

    def ciaone(self):
        self.count = self.count + 1
        self.text_output = tk.Label(self.window, text="Stub" + str(self.count), fg="green", font=("Helevetica", 16))
        self.text_output.grid(row=3, column=1, padx=50, sticky="W")

    def setRoom(self, sr):
        self.sr = sr
    
    def getWindow(self):
        return self.window