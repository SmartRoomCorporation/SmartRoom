from SmartRoom import SmartRoom
from modules.SensorModule.TempModule.TempModuleStub import TempModuleStub
import time
import tkinter as tk

sr = SmartRoom()
tm = TempModuleStub()
sr.addSensor("temp1", tm)
sr.setIp("87.16.33.82")
sr.start()
window = tk.Tk()
window.geometry("600x600")
window.title("SmartRoom")


def callSr():
    sr.pubToServ()

first_button = tk.Button(text="Click 1", command=callSr)
first_button.grid(row=0, column=0,sticky="W")

window.mainloop()
    