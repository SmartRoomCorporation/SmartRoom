from SmartRoom import SmartRoom
from modules.SensorModule.TempModule.TempModule import TempModule

sr = SmartRoom()
tm = TempModule()
sr.addSensor("temp1", tm)
sr.initClient("87.16.33.82")
