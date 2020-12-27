import tkinter as tk
import json

class Gui:
    window = tk.Tk()
    window.geometry("1200x600")
    window.title("SmartRoom")
    sr = ""
    text_output = ""
    count = 0
    camPreview = tk.Label(window, image = None, width=440, height=300)
    camPreview.grid(row=2)

    def run(self):
        self.initGui()
        self.refreshMeasure()
        self.refreshCamera()
        self.window.mainloop()

    def initGui(self):
        s_button = tk.Button(text="OPEN CAMERA", command=self.ciaone1)
        s_button.grid(row=4, column=0,sticky="W")
        s_button = tk.Button(text="CLOSE CAMERA", command=self.ciaone2)
        s_button.grid(row=5, column=0,sticky="W")     
        s_button = tk.Button(text="SET FULLSCREEN", command=self.ciaone)
        s_button.grid(row=6, column=0,sticky="W")                 

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
        self.camPreview.config(image = photo)
        self.camPreview.image = photo

    def ciaone(self):
        self.sr.getCamera().setFullScreen()

    def ciaone1(self):
        self.sr.getCamera().openCamera()

    def ciaone2(self):
        self.sr.getCamera().closeCamera()

    def setRoom(self, sr):
        self.sr = sr
    
    def getWindow(self):
        return self.window