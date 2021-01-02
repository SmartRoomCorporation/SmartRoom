import tkinter as tk
import json
from SensorListFrame import SensorListFrame

class Gui:
    window = tk.Tk()
    window.geometry()
    window.title("SmartRoom")
    sr = ""
    text_output = ""
    count = 0
    sensor_frame=""
    camera_frame=""
    camPreview=""

    def run(self):
        self.initGui()
        self.refreshMeasure()
        self.refreshCamera()
        self.window.mainloop()

    def initGui(self):
        self.sensor_frame=tk.Frame(self.window)
        self.sensor_frame.pack(expand=1,fill=tk.BOTH)
        sensor_list=SensorListFrame(self.sensor_frame,self.sr.getSensorsList())
        sensor_list.initGUI()
        sensor_list.pack(expand=1,fill=tk.BOTH,padx=5,pady=5)
        label=tk.Label(text="Door Status:",fg="blue")
        self.camera_frame=tk.LabelFrame(self.window,labelwidget=label,bd=1,relief="sunken")
        self.camera_frame.pack(expand=1,fill=tk.BOTH,padx=5,pady=5)
        frame=tk.Frame(self.camera_frame)
        frame.grid(sticky="W",row=0,column=0)
        self.camPreview = tk.Label(frame, image = None, width=440, height=300)
        self.camPreview.pack(expand=1,fill=tk.BOTH,padx=5,pady=5)
        frame1=tk.Frame(self.camera_frame)
        frame1.grid(row=0,column=1)
        s_button = tk.Button(frame1,text="OPEN CAMERA", command=self.openCamera)
        s_button.grid(row=0, column=0,sticky="W")
        s_button = tk.Button(frame1,text="CLOSE CAMERA", command=self.closeCamera)
        s_button.grid(row=1, column=0,sticky="W")

    def callSr(self):
        for key,value in self.sr.getSensorsList().items():
            value.startMeasure()
            value.actuator()
            value.refreshCurrValueLabel()
            #self.sr.updateReq(key, value.getSensorStatus())

    def refreshMeasure(self):
        self.callSr()
        self.window.after(2500, self.refreshMeasure)

    def refreshCamera(self):
        self.showCamera()
        self.sr.getCamera().showFaceRecon()
        self.window.after(int(1000/30), self.refreshCamera)

    def showCamera(self):
        photo = self.sr.getCamera().getCameraSimpleStream()
        self.camPreview.config(image = photo)
        self.camPreview.image = photo

    def openCamera(self):
        self.sr.getCamera().openCamera()

    def closeCamera(self):
        self.sr.getCamera().closeCamera()

    def setRoom(self, sr):
        self.sr = sr

    def getWindow(self):
        return self.window
