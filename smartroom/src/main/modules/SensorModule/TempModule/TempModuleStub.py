from .. import SensorModule

class TempModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function
	count = 0

	def startMeasure(self):
		if (self.count == 0):
			self.count = self.count + 1
			return self.setCurrValue(20)

		elif (self.count > 0 and self.count < 20):
			if (self.count % 3) == 0:
				if (self.getCurrValue() > 10): self.setCurrValue(self.getCurrValue() - 1)
				else: self.setCurrValue(self.getCurrValue() + 1)

		elif (self.count > 30 and self.count < 60):
			if (self.count % 3) == 0:
				if (self.getCurrValue() < 28): self.setCurrValue(self.getCurrValue() + 1)
				else: self.setCurrValue(self.getCurrValue() - 1)

		elif (self.count > 70): self.count = 0

		self.count = self.count + 1
		return self.getCurrValue()
