import tkinter as tk 
import os,sys,inspect

class SensorModule:
	curr_value = 0
	left_side = ""
	right_side = ""
	threshold_value = 0
	actuator_status = 0
	req_number = 10
	autopilot = True
	sensorname=""

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
		label=tk.Label(text=self.sensorname,fg="Green",font=("Helevetica",16))
		mainframe=tk.LabelFrame(block,labelwidget=label)
		mainframe.pack(fill=tk.X)
		frame1 = tk.Frame(mainframe)
		frame2 = tk.Frame(mainframe)
		frame1.grid(row=0, column=0)
		frame2.grid(row=0, column=1)
		self.left_side=frame1
		self.right_side=frame2
	
	def initGui(self,block):
		return 0

	def getSensorStatus(self): 
		return [self.getCurrValue(), self.getThresholdValue(), self.getActuatorStatus(), self.getAutoPilot()]

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

	def getAutoPilot(self): 
		return self.autopilot
	
	def getSensorName(self):
		return self.sensorname
	
	def setSensorName(self,val):
		self.sensorname=val

	def refreshCurrValueLabel(self):
		return 0

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