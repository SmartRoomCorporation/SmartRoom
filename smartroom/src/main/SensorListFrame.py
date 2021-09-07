import tkinter as tk
from VerticalScrolledFrame import VerticalScrolledFrame
from pprint import pprint

class SensorListFrame(tk.Frame):

    def __init__(self,parent,sensors,*args,**kv):
        super().__init__(master=parent,*args,**kv)
        self.parent=parent
        self.sensors=sensors
        

    def initGUI(self):
        
        label=tk.Label(text="Sensors:",fg="blue")
        self.frame=VerticalScrolledFrame(self,labelwidget=label)
        self.frame.pack(expand=1,fill=tk.BOTH)

        for key,value in self.sensors.items():
            #frame1=tk.Frame(self.frame.interior)
            #frame1.config(bd=1,relief="sunken")
            #frame1.pack(fill=tk.X,padx=5,pady=5)
            value.initGui(self.frame.interior)

    def addSensor(self, sensor):
        sensor.initGui(self.frame.interior)
      
