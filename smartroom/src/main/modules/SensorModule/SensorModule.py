import tkinter as tk 
import os,sys,inspect

class SensorModule:
	curr_value = 0
	left_side = ""
	right_side = ""
	threshold_value = 0
	actuator_status = 0
	req_number = 0
	autopilot = True

	def getResDir(self): 
		current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
		parent_dir = os.path.dirname(current_dir) 
		dirname = os.path.dirname(parent_dir) 
		return str(dirname)

	def setCurrValue(self, curr_value):
		self.curr_value = curr_value

	def getCurrValue(self):
		return self.curr_value

	def startMeasure(self):
		return 0

	def createGUIBlock(self, block):
		frame1 = tk.Frame(block)
		frame2 = tk.Frame(block)
		frame1.configure(highlightbackground="black", highlightcolor="black", highlightthickness=1, width=350, height=200, bd= 0,bg="grey")
		frame2.configure(highlightbackground="black", highlightcolor="black", highlightthickness=0.5, width=550, height=200, bg="white")
		frame1.grid(row=0, column=0)
		frame2.grid(row=0, column=1)
		self.left_side=frame1
		self.right_side=frame2

	def getSensorStatus(self): 
		return [self.getCurrValue(), self.getThresholdValue(), self.getActuatorStatus(), self.getAutopilot()]

	def getReqNumber(self): 
		return self.req_number

	def setReqNumber(self, n): 
		self.req_number = n
	
	def setThresholdValue(self, val): 
		self.threshold_value = val

	def getThresholdValue(self): 
		return self.threshold_value

	def getActuatorStatus(self): 
		return self.actuator_status

	def setActuatorStatus(self, status): 
		self.actuator_status = status
	
	def setAutoPilot(self, val): 
		self.autopilot = val

	def getAutopilot(self): 
		return self.autopilot

	def manualCommand(self): 
		return 0

	def actuator(self): 
		return 0

	def rise(self): 
		return 0

	def reduce(self): 
		return 0

	def serverCommand(self): 
		return 0