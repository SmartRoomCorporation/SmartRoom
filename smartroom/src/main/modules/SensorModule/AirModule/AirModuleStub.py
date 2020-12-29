from .. import SensorModule

class AirModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function
	count = 0
	MAXREQNUMBER = 12
	FANOFF = 0
	FANMIDDLE = 50
	FANFULL = 100
	LOWERBOUND = -1
	UPPERBOUND = 201

	def __init__(self): 
		self.setActuatorStatus(0)

	def initGui(self, block): 
		super().createGUIBlock(block) 

	def manualCommand(self, val): 
		self.setActuatorStatus(val)

	def actuator(self): 
		if(self.getCurrValue() <= self.LOWERBOUND or self.getCurrValue() >= self.UPPERBOUND): 
			self.setActuatorStatus(None)   
			return False   
		if(self.getAutopilot()): 
			if(self.getReqNumber() < self.MAXREQNUMBER): self.setReqNumber(self.getReqNumber() + 1) 
			else: 
				curr = self.getCurrValue()
				threshold = self.getThresholdValue()
				self.setReqNumber(0) 
				if(curr > (threshold + int(threshold/2))): self.setActuatorStatus(self.FANOFF) 
				elif(curr > threshold and curr < (threshold + int(threshold/2))): self.setActuatorStatus(self.FANMIDDLE)
				elif(curr < threshold): self.setActuatorStatus(self.FANFULL)

	def startMeasure(self):
		if self.count == 0:
			self.count = self.count + 1
			return self.setCurrValue(80)

		if self.count > 0 and self.count < 20:
			if (self.count % 3) == 0:
				if self.getCurrValue() > 50: self.setCurrValue(self.getCurrValue() - 2)
				else: self.setCurrValue(self.getCurrValue() + 1)
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
