from SmartRoom import SmartRoom
from Gui import Gui
from modules.SensorModule.TempModule.TempModuleStub import TempModuleStub
import time

sr = SmartRoom()
gui = Gui()
tm = TempModuleStub()
sr.addSensor("temp1", tm)
sr.setIp("87.16.33.82")
sr.start()
gui.setRoom(sr)
gui.run()


    