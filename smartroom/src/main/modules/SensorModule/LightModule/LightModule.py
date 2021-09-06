from .. import SensorModule
from PIL import Image, ImageTk
import tkinter as tk
from .. import ActuatorStatusBar
from .. import StatusCircle

class LightModule(SensorModule.SensorModule):
    #This module implements the temperature control function
	count = 0
	MAXREQNUMBER = 2
	DIMMEROFF = 0
	DIMMERMIDDLE = 50
	DIMMERFULL = 100
	LOWERBOUND = -1
	UPPERBOUND = 10001
	LIGHTUP = "LIGHTUP"
	LIGHTDOWN = "LIGHTDOWN"
	leftGuiSide = ""
	rightGuiSide = ""
	initGUI = False

	def __init__(self):
		self.setActuatorStatus(0)
		self.setThresholdValue(5000)

	def initGui(self, block):
		self.initGUI = True
		super().setSensorName("LightSensor")
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
				if(curr > (threshold + int(threshold/2))): self.setActuatorStatus(self.DIMMEROFF)
				elif(curr > threshold and curr < (threshold + int(threshold/2))): self.setActuatorStatus(self.DIMMERMIDDLE)
				elif(curr < threshold): self.setActuatorStatus(self.DIMMERFULL)

	def startMeasure(self):
		return self.getCurrValue()

	def getCount(self):
		return self.count

	def setCount(self, val):
		self.count = val

	def rise(self):
		currentTh = self.getThresholdValue()
		newTh = currentTh + 500
		if(newTh >= 10000): self.setThresholdValue(10000)
		else: self.setThresholdValue(newTh)

	def reduce(self):
		currentTh = self.getThresholdValue()
		newTh = currentTh - 500
		if(newTh <= 0): self.setThresholdValue(0)
		else: self.setThresholdValue(newTh)

	def serverCommand(self, data):
		if(not self.getAutoPilot()):
			if(data == self.LIGHTUP):
				currentLight = self.getActuatorStatus()
				if(currentLight == self.DIMMERMIDDLE): self.manualCommand(self.DIMMERFULL)
				elif(currentLight == self.DIMMEROFF): self.manualCommand(self.DIMMERMIDDLE)
			elif(data == self.LIGHTDOWN):
				currentLight = self.getActuatorStatus()
				if(currentLight == self.DIMMERMIDDLE): self.manualCommand(self.DIMMEROFF)
				elif(currentLight == self.DIMMERFULL): self.manualCommand(self.DIMMERMIDDLE)
			self.refreshCurrValueLabel()


	def createTempGui(self,left,right):
		up=Image.open(self.getResDir()+ "/res/assets/general/up.png")
		up=up.resize((20,20))
		self.up_icon=ImageTk.PhotoImage(up)
		up1=Image.open(self.getResDir()+ "/res/assets/general/down.png")
		up1=up1.resize((20,20))
		self.up_icon1=ImageTk.PhotoImage(up1)
		#STATUS FRAME
		label=tk.Label(left,text="Lumen:",fg="Black",font=("Helevetica",13))
		label.grid(row=2,column=1,padx=5,sticky="W")
		self.curr_output=tk.Label(left,text=self.getCurrValue(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
		self.curr_output.grid(row=2,column=2,padx=5,sticky="W")
		#CONTROL FRAME
		label=tk.Label(right,text="Threshold:",fg="Black",font=("Helevetica",13))
		label.grid(row=1,column=1,padx=5,pady=10,sticky="W")
		self.th_output=tk.Label(right,text=self.getThresholdValue(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
		self.th_output.grid(row=1,column=2,padx=5,pady=10)
		self.thup_button=tk.Button(right,image=self.up_icon,command=lambda:self.onThRise())
		self.thup_button.grid(row=1,column=3,padx=1)
		self.thdown_button=tk.Button(right,image=self.up_icon1,command=lambda:self.onThReduce())
		self.thdown_button.grid(row=1,column=4,padx=1)
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
		if(not self.initGUI): return False
		self.curr_output.config(text=self.getCurrValue())
		self.curr_output.update()
		self.th_output.config(text=self.getThresholdValue())
		self.th_output.update()
		if(self.actuator_status == self.DIMMEROFF):
			self.act_status.changeStatus(0)
		if(self.actuator_status == self.DIMMERMIDDLE):
			self.act_status.changeStatus(1)
		if(self.actuator_status == self.DIMMERFULL):
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
		self.serverCommand(self.LIGHTUP)


	def onActuatorReduce(self):
		self.serverCommand(self.LIGHTDOWN)

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