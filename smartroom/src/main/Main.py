from SmartRoom import SmartRoom
from modules.SensorModule.TempModule.TempModuleStub import TempModuleStub

sr = SmartRoom()
tm = TempModuleStub()
sr.addSensor("temp1", tm)
sr.initClient("87.16.33.82")
