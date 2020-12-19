import time
from ...SensorModule import SensorModule

class TempModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function

	def startMeasure(self):
		return 0