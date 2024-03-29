import tkinter as tk
from Sensors.StatusCircle import StatusCircle

class TempSensor:
    autopilot = True
    actuator = False
    ON = True
    OFF = False
    current_val = 0
    threshold_val = 0
    gui = False
    smartroom = ""
    COMMAND = "COMMAND"
    AUTOOFF = "AUTOOFF"
    AUTOON = "AUTOON"
    ACTUATOR = "ACTUATOR"
    RISE = "RISE"
    REDUCE = "REDUCE"
    SENSOR = "Temperature"
    REQON = "ON"
    REQOFF = "OFF"
    humidity = 0
    temperature = 0

    def __init__(self, smartroom):
        self.smartroom = smartroom

    def setGui(self, val):
        self.gui = val

    def setAutoPilot(self, val):
        self.autopilot = val

    def setActuator(self, val):
        self.actuator = val

    def setCurrentValue(self, val):
        self.temperature = val[0]
        self.humidity = val[1]

    def getAutopilot(self):
        return self.autopilot

    def getActuator(self):
        return self.actuator

    def getCurrentValue(self):
        return self.current_val

    def setThresholdValue(self, val):
        self.threshold_val = val

    def getThresholdValue(self):
        return self.threshold_val

    def createTempGui(self, block):
        label=tk.Label(text="Temperature Sensor",fg="Green",font=("Helevetica",16))
        mainframe=tk.LabelFrame(block,labelwidget=label)
        mainframe.pack(expand = 1,fill=tk.X)
        frame1 = tk.Frame(mainframe)
        frame2 = tk.Frame(mainframe)
        frame1.grid(row=0, column=0)
        frame2.grid(row=0, column=1)
        left=frame1
        right=frame2
#        up = Image.open(self.getResDir() + "/res/assets/general/up.png")
#        up = up.resize((20, 20))
#        self.up_icon = ImageTk.PhotoImage(up)
#        up1 = Image.open(self.getResDir() + "/res/assets/general/down.png")
#        up1 = up1.resize((20, 20))
#        self.up_icon1 = ImageTk.PhotoImage(up1)
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
        thup_button=tk.Button(right,text = "+",command=lambda:self.reqRiseThreshold())
        thup_button.grid(row=1,column=3,padx=1)
        thdown_button=tk.Button(right,text = "-",command=lambda:self.reqReduceThreshold())
        thdown_button.grid(row=1,column=4,padx=1)
        label=tk.Label(right,text="Actuator:",fg="Black",font=("Helevetica",13))
        label.grid(row=1,column=5,padx=5,pady=10,sticky="W")
        self.act_status=StatusCircle(right,height=30,width=30)
        self.act_status.grid(row=1,column=6,padx=5,pady=5)
        acup_button=tk.Button(right,text="ON",command=lambda:self.reqActuatorOn())
        acup_button.grid(row=1,column=7,padx=1)
        acdown_button=tk.Button(right,text="OFF",command=lambda:self.reqActuatorOff())
        acdown_button.grid(row=1,column=8,padx=1)
        label=tk.Label(right,text="Autopilot:",fg="Black",font=("Helevetica",13))
        label.grid(row=1,column=9,padx=5,pady=10,sticky="W")
        self.auto_output=StatusCircle(right,height=30,width=30)
        self.auto_output.change()
        self.auto_output.grid(row=1,column=10,padx=5,pady=10)
        auto_button=tk.Button(right,text="ON-OFF",command=lambda:self.reqChangeAutoPilot())
        auto_button.grid(row=1,column=11,padx=5)

    def updateGui(self):
        if self.gui:
            self.curr_outputT.config(text = self.getCurrTemperature())
            self.curr_outputH.config(text = self.getCurrHumidity())
            self.th_output.config(text = self.getThresholdValue())
            if self.getActuator() == self.ON:
                self.act_status.change(True)
            if self.getActuator() == self.OFF:
                self.act_status.change(False)

            self.auto_output.change(self.getAutopilot())

    def getCurrHumidity(self):
        return self.humidity

    def getCurrTemperature(self):
        return self.temperature

    def reqChangeAutoPilot(self):
        status = ""
        if(self.autopilot):
            self.setAutoPilot(False)
            status = self.AUTOOFF
        else:
            self.setAutoPilot(True)
            status = self.AUTOON
        data = [self.SENSOR, status]
        command = [self.COMMAND, data]
        self.smartroom.getServerInstance().sendCommand(self.smartroom.getMacAddress(), command)

    def reqRiseThreshold(self):
        data = [self.SENSOR, self.RISE]
        command = [self.COMMAND, data]
        self.smartroom.getServerInstance().sendCommand(self.smartroom.getMacAddress(), command)

    def reqReduceThreshold(self):
        data = [self.SENSOR, self.REDUCE]
        command = [self.COMMAND, data]
        self.smartroom.getServerInstance().sendCommand(self.smartroom.getMacAddress(), command)

    def reqActuatorOn(self):
        data = [self.SENSOR, self.ACTUATOR, self.REQON]
        command = [self.COMMAND, data]
        self.smartroom.getServerInstance().sendCommand(self.smartroom.getMacAddress(), command)

    def reqActuatorOff(self):
        data = [self.SENSOR, self.ACTUATOR, self.REQOFF]
        command = [self.COMMAND, data]
        self.smartroom.getServerInstance().sendCommand(self.smartroom.getMacAddress(), command)
