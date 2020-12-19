import time
import board
import adafruit_dht as ad

class TempModule(SensorModule):
    #This module implements the temperature control function
	data_pin = 0
	def _init_(self, ref_value, data_pin)
		super()._init_(self, ref_value)
		self.data_pin = 

	def startMeasure(self):
		try:
			temp = 
