from SmartRoom import SmartRoom
from Gui import Gui
from modules.SensorModule.TempModule.TempModuleStub import TempModuleStub
from modules.SensorModule.LightModuleSD.LightModuleSD import LightModuleSD
from modules.SensorModule.AirModule.AirModuleStub import AirModuleStub
from modules.SensorModule.TempHumModule.TempHumModule import TempHumModule
from modules.FaceRecon.Camera import Camera
import time


sr = SmartRoom()
#camera = Camera()
#camera.initCamera()
gui = Gui()
#tm = TempModuleStub()
thm = TempHumModule()
lm = LightModuleSD()
#am = AirModuleStub()
#sr.setCamera(camera)
sr.addSensor("TemperatureHumidity", thm)
#sr.addSensor("Temperature", tm)
sr.addSensor("Light", lm)
#sr.addSensor("Air", am)
sr.setIp("87.7.152.200")
sr.start()
gui.setRoom(sr)
gui.run()
