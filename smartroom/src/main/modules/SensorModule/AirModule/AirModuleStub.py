from .. import SensorModule
from PIL import Image, ImageTk
import tkinter as tk
from .. import ActuatorStatusBar 
from .. import StatusCircle

class AirModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function
	count = 0
	MAXREQNUMBER = 2
	FANOFF = 0
	FANMIDDLE = 50
	FANFULL = 100
	LOWERBOUND = -1
	UPPERBOUND = 201
	FANUP = "FANUP"
	FANDOWN = "FANDOWN"
	leftGuiSide = ""
	rightGuiSide = ""

	def __init__(self):
		self.setThresholdValue(100)
		self.setActuatorStatus(0)

	def initGui(self, block):
		super().setSensorName("AirModule")
		super().createGUIBlock(block)
		self.leftGuiSide = self.left_side
		self.rightGuiSide = self.right_side
		self.createTempGui(self.leftGuiSide, self.rightGuiSide)

	def manualCommand(self, val):
		self.setActuatorStatus(val)

	def actuator(self):
		if(self.getCurrValue() <= self.LOWERBOUND or self.getCurrValue() >= self.UPPERBOUND):
			self.setActuatorStatus(None)
			return False
		if(self.getAutoPilot()):
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
		if(not self.getAutoPilot()):
			if(data == self.FANUP):
				currentSpeed = self.getActuatorStatus()
				if(currentSpeed == self.FANMIDDLE): self.manualCommand(self.FANFULL)
				elif(currentSpeed == self.FANOFF): self.manualCommand(self.FANMIDDLE)
			elif(data == self.FANDOWN):
				currentSpeed = self.getActuatorStatus()
				if(currentSpeed == self.FANMIDDLE): self.manualCommand(self.FANOFF)
				elif(currentSpeed == self.FANFULL): self.manualCommand(self.FANMIDDLE)
			self.refreshCurrValueLabel()
				

	def createTempGui(self,left,right):
		up=Image.open(self.getResDir()+ "/res/assets/general/up.png")
		up=up.resize((20,20))
		self.up_icon=ImageTk.PhotoImage(up)
		up1=Image.open(self.getResDir()+ "/res/assets/general/down.png")
		up1=up1.resize((20,20))
		self.up_icon1=ImageTk.PhotoImage(up1)
		#STATUS FRAME
		label=tk.Label(left,text="Quality:",fg="Black",font=("Helevetica",13))
		label.grid(row=2,column=1,padx=5,sticky="W")
		self.curr_output=tk.Label(left,text=self.getCurrValue(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
		self.curr_output.grid(row=2,column=2,padx=5,sticky="W")
		#CONTROL FRAME
		label=tk.Label(right,text="Threshold:",fg="Black",font=("Helevetica",13))
		label.grid(row=1,column=1,padx=5,pady=10,sticky="W")
		self.th_output=tk.Label(right,text=self.getThresholdValue(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
		self.th_output.grid(row=1,column=2,padx=5,pady=10)
		thup_button=tk.Button(right,image=self.up_icon,command=lambda:self.onThRise())
		thup_button.grid(row=1,column=3,padx=1)
		thdown_button=tk.Button(right,image=self.up_icon1,command=lambda:self.onThReduce())
		thdown_button.grid(row=1,column=4,padx=1)
		label=tk.Label(right,text="Actuator:",fg="Black",font=("Helevetica",13))
		label.grid(row=1,column=5,padx=5,pady=10,sticky="W")
		self.act_status=ActuatorStatusBar.ActuatorStatusBar(right)
		self.act_status.grid(row=1,column=6,padx=5,pady=5)
		acup_button=tk.Button(right,image=self.up_icon,command=lambda:self.onActuatorRise())
		acup_button.grid(row=1,column=7,padx=1)
		acdown_button=tk.Button(right,image=self.up_icon1,command=lambda:self.onActuatorReduce())
		acdown_button.grid(row=1,column=8,padx=1)
		label=tk.Label(right,text="Autopilot:",fg="Black",font=("Helevetica",13))
		label.grid(row=1,column=9,padx=5,pady=10,sticky="W")
		self.auto_output=StatusCircle.StatusCircle(right,height=30,width=30)
		self.auto_output.change()
		self.auto_output.grid(row=1,column=10,padx=5,pady=10)
		auto_button=tk.Button(right,text="ON-OFF",command=lambda:self.onChangeAutopilot())
		auto_button.grid(row=1,column=11,padx=5)

	def refreshCurrValueLabel(self):
		self.curr_output.config(text=self.getCurrValue())
		self.curr_output.update()
		if(self.actuator_status == self.FANOFF):
			self.act_status.changeStatus(0)
		if(self.actuator_status == self.FANMIDDLE):
			self.act_status.changeStatus(1)
		if(self.actuator_status == self.FANFULL):
			self.act_status.changeStatus(2)
		self.autoPilotStatusLED()
	
	def onThRise(self):
		self.rise()
		self.th_output.config(text=self.getThresholdValue())
		self.th_output.update()

	def onThReduce(self):
		self.reduce()
		self.th_output.config(text=self.getThresholdValue())
		self.th_output.update()

	def onActuatorRise(self):
		self.serverCommand(self.FANUP)
	

	def onActuatorReduce(self):	
		self.serverCommand(self.FANDOWN)

	def onChangeAutopilot(self):
		if(self.getAutoPilot()):
			self.setAutoPilot(False)
		else:
			self.setAutoPilot(True)
		self.auto_output.change()
	
	def autoPilotStatusLED(self): 
		if(self.getAutoPilot()): 
			self.auto_output.change(True) 
		else: 
			self.auto_output.change(False)