from .. import SensorModule
from PIL import Image, ImageTk
import tkinter as tk
from .. import ActuatorStatusBar
from .. import StatusCircle
import random


class TempHumModule(SensorModule.SensorModule):
    #This module implements the temperature control function
    count = 0
    leftGuiSide = ""
    rightGuiSide = ""
    MAXREQNUMBER = 12
    UPPERBOUND = 80
    LOWERBOUND = -50
    UPPERBOUNDTHRESHOLD = 30
    LOWERBOUNDTHRESHOLD = 18
    ON = "ON"
    OFF = "OFF"
    initGUI = False
    temperature = 0
    humidity = 0

    def __init__(self):
        self.setThresholdValue(25)
        #self.setActuatorStatus(False)

    def initGui(self, block):
        self.initGUI = True
        super().createGUIBlock(block)
        self.leftGuiSide = self.left_side
        self.rightGuiSide = self.right_side
        self.createTempGui(self.leftGuiSide, self.rightGuiSide)

    def manualCommand(self, val):
        self.setAutoPilot(val)
        if(not val): self.setActuatorStatus(val)

    def actuator(self):
        if(self.getCurrTemperature() < self.LOWERBOUND or self.getCurrTemperature() > self.UPPERBOUND):
            return self.setActuatorStatus(None)
        if(self.getAutoPilot()):
            if(self.getReqNumber() < self.MAXREQNUMBER): self.setReqNumber(self.getReqNumber() + 1)
            else:
                self.setReqNumber(0)
                if(self.getCurrTemperature() > self.getThresholdValue()): self.setActuatorStatus(False)
                else: self.setActuatorStatus(True)

    def startMeasure(self):
        self.temperature = random.randint(0, 9)
        self.humidity = random.randint(0, 9)
        val = [self.getCurrTemperature(), self.getCurrHumidity()]
        return val

    def getCurrValue(self):
        val = [self.getCurrTemperature(), self.getCurrHumidity()]
        return val

    def getCount(self):
        return self.count

    def setCount(self, val):
        self.count = val

    def rise(self):
        currentTh = self.getThresholdValue()
        newTh = currentTh + 1
        if(newTh >= self.UPPERBOUNDTHRESHOLD): self.setThresholdValue(self.UPPERBOUNDTHRESHOLD)
        else: self.setThresholdValue(newTh)

    def reduce(self):
        currentTh = self.getThresholdValue()
        newTh = currentTh - 1
        if(newTh <= self.LOWERBOUNDTHRESHOLD): self.setThresholdValue(self.LOWERBOUNDTHRESHOLD)
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
        self.curr_outputT=tk.Label(left,text=self.getCurrTemperature(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
        self.curr_outputT.grid(row=2,column=2,padx=5,sticky="W")
        label=tk.Label(left,text="Humidity:",fg="Black",font=("Helevetica",13))
        label.grid(row=3,column=1,padx=5,sticky="W")
        self.curr_outputH=tk.Label(left,text=self.getCurrHumidity(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
        self.curr_outputH.grid(row=3,column=2,padx=5,sticky="W")
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
        if(not self.initGUI): return False
        self.curr_outputT.config(text=self.getCurrTemperature())
        self.curr_outputT.update()
        self.curr_outputH.config(text=self.getCurrHumidity())
        self.curr_outputH.update()
        self.th_output.config(text=self.getThresholdValue())
        self.th_output.update()
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
    
    def setCurrTemperature(self, val):
        self.temperature = val

    def setCurrHumidity(self, val):
        self.humidity = val

    def getCurrTemperature(self):
        return self.temperature

    def getCurrHumidity(self):
        return self.humidity

    def setActuatorStatus(self, status):
        wrapper = dict() 
        comm = dict() 
        wrapper["msgType"] = "COMMAND" 
        comm["setwh"] = status 
        wrapper["command"] = comm 
        self.getSmartroom().sendDirectCommand(self.getMac(), wrapper) 
        self.actuator_status = status

    def readMeasures(self, payload): 
        self.setCurrTemperature(int(payload["temperature"])) 
        self.setCurrHumidity(int(payload["humidity"]))