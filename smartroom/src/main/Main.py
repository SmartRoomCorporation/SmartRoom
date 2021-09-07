from SmartRoom import SmartRoom
from Gui import Gui
from modules.SensorModule.TempModule.TempModuleStub import TempModuleStub
from modules.SensorModule.LightModule.LightModuleStub import LightModuleStub
from modules.SensorModule.AirModule.AirModuleStub import AirModuleStub
from modules.FaceRecon.Camera import Camera
import time


sr = SmartRoom()
camera = Camera()
camera.initCamera()
sr.setCamera(camera)
gui = Gui()

sr.setGui(gui)

sr.setIp("79.12.248.28")
sr.start()
gui.setRoom(sr)
gui.run()

#tm = TempModuleStub()
#lm = LightModuleStub()
#am = AirModuleStub()

#sr.addSensor("Temperature", tm)
#sr.addSensor("Light", lm)
#sr.addSensor("Air", am)


