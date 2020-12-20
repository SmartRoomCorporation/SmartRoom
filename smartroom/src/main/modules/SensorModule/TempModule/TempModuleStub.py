import time
from random import randint
from ...SensorModule import SensorModule

class TempModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function

	def startMeasure(self):
		return randint(1,100)