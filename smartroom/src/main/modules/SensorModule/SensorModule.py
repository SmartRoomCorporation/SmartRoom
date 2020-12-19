class SensorModule:
	curr_value = 0

	def setCurrValue(self, curr_value):
		self.curr_value = curr_value

	def getCurrValue(self):
		return self.curr_value

	def startMeasure(self):
		return 0
