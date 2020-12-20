from .. import SensorModule

class LightModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function
	count = 0

	def startMeasure(self):
		if self.count == 0:
			self.count = self.count + 1
			return self.setCurrValue(1500)

		if self.count > 0 and self.count < 20:
			if (self.count % 3) == 0:
				if self.getCurrValue() > 1000:
					self.setCurrValue(self.getCurrValue() - 150)
                else:
                    self.setCurrValue(self.getCurrValue() + 80)

		if self.count > 30 and self.count < 60:
			if (self.count % 3) == 0:
				if self.getCurrValue() < 2500:
					self.setCurrValue(self.getCurrValue() + 150)
				else:
					self.setCurrValue(self.getCurrValue() - 100)

		if self.count > 70:
			self.count = 0

		self.count = self.count + 1
		return self.getCurrValue()
