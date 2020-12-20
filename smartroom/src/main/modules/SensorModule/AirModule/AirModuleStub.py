from .. import SensorModule

class AirModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function
	count = 0

	def startMeasure(self):
		if self.count == 0:
			self.count = self.count + 1
			return self.setCurrValue(80)

		if self.count > 0 and self.count < 20:
			if (self.count % 3) == 0:
				if self.getCurrValue() > 50:
					self.setCurrValue(self.getCurrValue() - 2)
                else:
                    self.setCurrValue(self.getCurrValue() + 1)

		if self.count > 30 and self.count < 60:
			if (self.count % 3) == 0:
				if self.getCurrValue() < 100:
					self.setCurrValue(self.getCurrValue() + 5)
				else:
					self.setCurrValue(self.getCurrValue() - 3)

		if self.count > 70:
			self.count = 0

		self.count = self.count + 1
		return self.getCurrValue()
