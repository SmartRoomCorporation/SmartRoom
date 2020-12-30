from .. import SensorModule
from PIL import Image, ImageTk
import tkinter as tk

class TempModuleStub(SensorModule.SensorModule):
    #This module implements the temperature control function
    count = 0
    leftGuiSide = ""
    rightGuiSide = ""
    MAXREQNUMBER = 12
    UPPERBOUND = 80
    LOWERBOUND = -50
    ON = "ON"
    OFF = "OFF" 

    def __init__(self):
        self.setActuatorStatus(False)
        self.setThresholdValue(25)

    def initGui(self, block):
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
        if(self.getAutopilot()): 
            if(self.getReqNumber() < self.MAXREQNUMBER): self.setReqNumber(self.getReqNumber() + 1)
            else:
                self.setReqNumber(0)
                if(self.getCurrValue() > self.getThresholdValue()): self.setActuatorStatus(False)
                else: self.setActuatorStatus(True)

    def startMeasure(self):
        if(self.count == 0):
            self.count = self.count + 1
            self.setCurrValue(15)
        if(self.count > 0 and self.count < 20):
            self.count = self.count + 1
            self.setCurrValue(16)
            if(self.count % 3 == 0):
                if (self.getCurrValue() > 10): 
                    self.setCurrValue(self.getCurrValue() - 1)
                else:
                    self.setCurrValue(self.getCurrValue() + 1)
        if(self.count > 30 and self.count < 60):
            self.setCurrValue(18)
            if(self.count % 3 == 0):
                if (self.getCurrValue() < 28): 
                    self.setCurrValue(self.getCurrValue() - 1)
                else:
                    self.setCurrValue(self.getCurrValue() + 1)
        if(self.count > 70):
            self.count = 0
        return self.getCurrValue()

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
        if(data == self.OFF): self.manualCommand(False)
        elif(data == self.ON): self.manualCommand(True)

    def getGUIBlock(self):
        return self.guiBlock

    def createTempGui(self, left, right):
        up = Image.open(self.getResDir() + "/res/assets/general/up.png")
        up = up.resize((20, 20))
        self.up_icon = ImageTk.PhotoImage(up)
        up1 = Image.open(self.getResDir() + "/res/assets/general/down.png")
        up1 = up1.resize((20, 20))
        self.up_icon1 = ImageTk.PhotoImage(up1)
        text_output = tk.Label(left, text="Sensore 1:", fg="Green", font=("Helevetica",16))
        text_output.grid(row=1, column=1, padx=50, sticky="W")
        text_output = tk.Label(left, text="valore:", fg="black", font=("Helevetica",13))
        text_output.grid(row=2, column=1, padx=50, sticky="W")
        text_output = tk.Label(left, text="Trigger:", fg="black", font=("Helevetica",13))
        text_output.grid(row=3, column=1, padx=50, sticky="W")
        first_button = tk.Button(right, image=self.up_icon)
        first_button.grid(row=1, column=1, padx=50, sticky="W")
        first_button = tk.Button(right, image=self.up_icon1)
        first_button.grid(row=2, column=1, padx=50, sticky="W")
        text_output = tk.Label(left, text="Stato: ",fg="black", font=("Helevetica",13))
        text_output.grid(row=4, column=1, padx=50, sticky="W")