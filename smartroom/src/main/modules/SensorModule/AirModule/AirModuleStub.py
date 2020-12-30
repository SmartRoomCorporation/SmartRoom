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
	FANUP = "FANUP"
	FANDOWN = "FANDOWN"

	def __init__(self):
		self.setThresholdValue(100)
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
			self.setCurrValue(80)
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

	def getCount(self): 
		return self.count

	def setCount(self, val):
		self.count = val

	def rise(self):
		currentTh = self.getThresholdValue()
		newTh = currentTh + 20
		if(newTh >= 200): self.setThresholdValue(200)
		else: self.setThresholdValue(newTh)

	def reduce(self):
		currentTh = self.getThresholdValue()
		newTh = currentTh - 20
		if(newTh <= 0): self.setThresholdValue(0)
		else: self.setThresholdValue(newTh)

	def serverCommand(self, data):
		if(data == self.FANUP):
			currentSpeed = self.getActuatorStatus()
			if(currentSpeed == self.FANMIDDLE): self.manualCommand(self.FANFULL)
			elif(currentSpeed == self.FANOFF): self.manualCommand(self.FANMIDDLE)
			return False
		if(data == self.FANDOWN):
			currentSpeed = self.getActuatorStatus()
			if(currentSpeed == self.FANMIDDLE): self.manualCommand(self.FANOFF)
			elif(currentSpeed == self.FANFULL): self.manualCommand(self.FANMIDDLE)
			return False
