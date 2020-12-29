from SmartRoom import SmartRoom
from Gui import Gui
from modules.SensorModule.TempModule.TempModuleStub import TempModuleStub
from modules.FaceRecon.Camera import Camera
import time


sr = SmartRoom()
camera = Camera()
camera.initCamera()
gui = Gui()
tm = TempModuleStub()
tm.initGui(gui.getWindow())
sr.setCamera(camera)
sr.addSensor("temp1", tm)
sr.setIp("87.7.152.200")
sr.start()
gui.setRoom(sr)
gui.run()
