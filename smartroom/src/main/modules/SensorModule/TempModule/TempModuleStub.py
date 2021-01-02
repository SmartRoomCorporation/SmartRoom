from .. import SensorModule
from PIL import Image, ImageTk
import tkinter as tk
from .. import ActuatorStatusBar 
from .. import StatusCircle


class TempModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function
    count = 0
    leftGuiSide = ""
    rightGuiSide = ""
    MAXREQNUMBER = 2
    UPPERBOUND = 80
    LOWERBOUND = -50
    ON = "ON"
    OFF = "OFF"

    def __init__(self):
        self.setActuatorStatus(False)
        self.setThresholdValue(25)

    def initGui(self, block):
        super().setSensorName("TemperatureSensor")
        super().createGUIBlock(block)
        self.leftGuiSide = self.left_side
        self.rightGuiSide = self.right_side
        self.createTempGui(self.leftGuiSide, self.rightGuiSide)

    def manualCommand(self, val):
        self.setAutoPilot(val)
        if(not val): self.setActuatorStatus(val)

    def actuator(self):
        if(self.getCurrValue() < self.LOWERBOUND or self.getCurrValue() > self.UPPERBOUND):
            return self.setActuatorStatus(None)
        if(self.getAutoPilot()):
            if(self.getReqNumber() < self.MAXREQNUMBER): self.setReqNumber(self.getReqNumber() + 1)
            else:
                self.setReqNumber(0)
                if(self.getCurrValue() > self.getThresholdValue()): self.setActuatorStatus(False)
                else: self.setActuatorStatus(True)

    def startMeasure(self):
        if(self.count == 0):
            self.setCurrValue(15)
        if(self.count > 0 and self.count < 20):
            if(self.count % 3 == 0):
                if (self.getCurrValue() > 10):
                    self.setCurrValue(self.getCurrValue() - 1)
                else:
                    self.setCurrValue(self.getCurrValue() + 1)
        if(self.count > 30 and self.count < 60):
            if(self.count % 3 == 0):
                if (self.getCurrValue() < 28):
                    self.setCurrValue(self.getCurrValue() - 1)
                else:
                    self.setCurrValue(self.getCurrValue() + 1)
        if(self.count > 70):
            self.count = 0
        self.count = self.count + 1
        return self.getCurrValue() 
        
    def getCount(self): 
        return self.count 
    
    def setCount(self, val): 
        self.count = val

    def rise(self):
        currentTh = self.getThresholdValue()
        newTh = currentTh + 1
        if(newTh >= 30): self.setThresholdValue(30)
        else: self.setThresholdValue(newTh)

    def reduce(self):
        currentTh = self.getThresholdValue()
        newTh = currentTh - 1
        if(newTh <= 18): self.setThresholdValue(18)
        else: self.setThresholdValue(newTh)

    def serverCommand(self, data):
        if(not self.getAutoPilot()):
            if(data == self.OFF): self.manualCommand(False)
            elif(data == self.ON): self.manualCommand(True)
            self.refreshCurrValueLabel()

    def getGUIBlock(self):
        return self.guiBlock

    def createTempGui(self, left, right):
        up = Image.open(self.getResDir() + "/res/assets/general/up.png")
        up = up.resize((20, 20))
        self.up_icon = ImageTk.PhotoImage(up)
        up1 = Image.open(self.getResDir() + "/res/assets/general/down.png")
        up1 = up1.resize((20, 20))
        self.up_icon1 = ImageTk.PhotoImage(up1)
        #STATUS FRAME
        label=tk.Label(left,text="Temperature:",fg="Black",font=("Helevetica",13))
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
        self.act_status=StatusCircle.StatusCircle(right,height=30,width=30)
        self.act_status.grid(row=1,column=6,padx=5,pady=5)
        acup_button=tk.Button(right,text="ON",command=lambda:self.onActuatorRise())
        acup_button.grid(row=1,column=7,padx=1)
        acdown_button=tk.Button(right,text="OFF",command=lambda:self.onActuatorReduce())
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
        if(self.getActuatorStatus()):
            self.act_status.change(True)
        else:
            self.act_status.change(False)
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
        self.serverCommand(self.ON)
        
    def onActuatorReduce(self): 
        self.serverCommand(self.OFF)
        
    def onChangeAutopilot(self): 
        if(self.getAutoPilot()): 
            self.setAutoPilot(False) 
            self.auto_output.change(False)
        else: 
            self.setAutoPilot(True) 
            self.auto_output.change(True)
    
    def autoPilotStatusLED(self):
        if(self.getAutoPilot()):
            self.auto_output.change(True)
        else:
            self.auto_output.change(False)