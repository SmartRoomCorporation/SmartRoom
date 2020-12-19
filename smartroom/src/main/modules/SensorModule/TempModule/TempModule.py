import time
import board
import adafruit_dht as ad

class TempModule(SensorModule):
    #This module implements the temperature control function
	dht = adafruit_dht(board.D4)

	def startMeasure(self):
		try:
			temp = dht.temperature
			super().setCurrValue(temp)
			return temp
		except RuntimeException as Error
			return super().getCurrValue()
		except Exceprion as Error
			return super().getCurrValue()
