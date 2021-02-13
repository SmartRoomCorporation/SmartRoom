from .. import SensorModule
from PIL import Image, ImageTk
import tkinter as tk
from .. import ActuatorStatusBar
from .. import StatusCircle
from .RoomConditioning import RoomConditioning


class TempHumModule(SensorModule.SensorModule):
    #This module implements the temperature control function
    r = RoomConditioning()
    leftGuiSide = ""
    rightGuiSide = ""
    temperature = 0
    humidity = 0
    tempcond = 0
    tempcalc = 0
    tempmod = 0
    humcond = 0
    humcalc = 0
    hummod = 0
    peoplecounted = 0
    people = 0
    alarm = 0
    fan = 0
    
    tempmodhistory = []
    tempcondhistory = []
    temperaturehistory = []
    tempcalchistory = []
    hummodhistory = []
    humcondhistory = []
    humidityhistory = []
    humcalchistory = []
    peoplehistory = []
    peoplecountedhistory = []
    initGUI = False


    UPPERBOUND = 80
    LOWERBOUND = -50
    UPPERBOUNDTHRESHOLD = 30
    LOWERBOUNDTHRESHOLD = 18
    ON = "ON"
    OFF = "OFF"
    MAXREQNUMBER = 12


    def __init__(self):
        self.setActuatorStatus(False)
        self.setThresholdValue(25)
        self.setActuatorStatus(False)

    def initGui(self, block):
        self.initGUI = True
        super().setSensorName("TemperatureHumiditySensor")
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
        self.r.tempmodGen()
        self.r.hummodGen()
        self.r.tempcondGen()
        self.r.humcondGen()
        self.r.computeTempcalc()
        self.r.computeHumcalc()
        self.temperature = self.r.room.temperature # EVOLUZIONE NATURALE
        self.temperaturehistory.append(self.temperature) 
        self.humidity = self.r.room.humidity # EVOLUZIONE NATURALE 
        self.humidityhistory.append(self.humidity)
        self.tempmod = self.r.tempmod # MODIFICATA DALLE PERSONE
        self.tempmodhistory.append(self.tempmod)
        self.hummod = self.r.hummod # MODIFICATA DALLE PERSONE
        self.hummodhistory.append(self.hummod)
        self.tempcond = self.r.tempcond # CONDIZIONATA DALLA VENTOLA
        self.tempcondhistory.append(self.tempcond)
        self.humcond = self.r.humcond # CONDIZIONATA DALLA VENTOLA
        self.humcondhistory.append(self.humcond)
        self.tempcalc = self.r.tempcalc # CALCOLATA DAL SISTEMA IN BASE ALLA CONDIZIONATA
        self.tempcalchistory.append(self.tempcalc)
        self.humcalc = self.r.humcalc # CALCOLATA DAL SISTEMA IN BASE ALLA CONDIZIONATA
        self.humcalchistory.append(self.humcalc)
        self.people = self.r.room.people # NUMERO DI PERSONE REALMENTE PRESENTI
        self.peoplehistory.append(self.people)
        self.peoplecounted = self.r.activateReading() # NUMERO DI PERSONE CALCOLATO
        self.peoplecountedhistory.append(self.peoplecounted)
        self.alarm = self.r.sys.alarm
        self.fan = self.r.sys.fan

    def printAllVals(self):
        print(self.tempcond)
    
    def getTempCond(self):
        return round(self.tempcond, 2)

    def getHumCond(self):
        return round(self.humcond, 2)

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
        label.grid(row=1,column=1,padx=5,sticky="W")
        self.curr_toutput=tk.Label(left,text=self.getTempCond(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
        self.curr_toutput.grid(row=1,column=2,padx=5,sticky="W")
        label=tk.Label(left,text="Humidity:",fg="Black",font=("Helevetica",13))
        label.grid(row=2,column=1,padx=5,sticky="W")
        self.curr_houtput=tk.Label(left,text=self.getHumCond(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
        self.curr_houtput.grid(row=2,column=2,padx=5,sticky="W")
		#CONTROL FRAME
        label=tk.Label(right,text="Actual People:",fg="Black",font=("Helevetica",13))
        label.grid(row=1,column=4,padx=5,pady=10,sticky="W")
        self.th_output=tk.Label(right,text=self.people,fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
        self.th_output.grid(row=1,column=5,padx=5,pady=10)
        thup_button=tk.Button(right,image=self.up_icon,command=lambda:self.onThRise())
        thup_button.grid(row=1,column=6,padx=1)
        thdown_button=tk.Button(right,image=self.up_icon1,command=lambda:self.onThReduce())
        thdown_button.grid(row=1,column=7,padx=1)
        label=tk.Label(right,text="Calculated People:",fg="Black",font=("Helevetica",13))
        label.grid(row=2,column=4,padx=5,pady=10,sticky="W")
        self.thc_output=tk.Label(right,text=round(self.peoplecounted, 1),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
        self.thc_output.grid(row=2,column=5,padx=5,pady=10)
        label=tk.Label(right,text="Fan:",fg="Black",font=("Helevetica",13))
        label.grid(row=1,column=9,padx=5,pady=10,sticky="W")
        self.thf_output=tk.Label(right,text=self.fan,fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
        self.thf_output.grid(row=1,column=10,padx=5,pady=10)
        label=tk.Label(right,text="Alarm:",fg="Black",font=("Helevetica",13))
        label.grid(row=2,column=9,padx=5,pady=10,sticky="W")
        self.auto_output=StatusCircle.StatusCircle(right,height=30,width=30)
        self.alarmLED()
        self.auto_output.grid(row=2,column=10,padx=5,pady=10)

    def refreshCurrValueLabel(self):
        if(not self.initGUI): return False
        self.curr_toutput.config(text=self.getTempCond())
        self.curr_toutput.update()
        self.curr_houtput.config(text=self.getHumCond())
        self.curr_houtput.update()
        self.th_output.config(text=self.people)
        self.th_output.update()
        self.thc_output.config(text=round(self.peoplecounted, 1))
        self.thc_output.update()
        self.thf_output.config(text=self.fan)
        self.thf_output.update()
        self.alarmLED()

    def onThRise(self):
        self.r.room.addPerson()
        self.th_output.config(text=self.people)
        self.th_output.update()

    def onThReduce(self):
        self.r.room.removePerson()
        self.th_output.config(text=self.people)
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

    def alarmLED(self):
        if(self.alarm > 0):
            self.auto_output.change(False)
        else:
            self.auto_output.change(True)
