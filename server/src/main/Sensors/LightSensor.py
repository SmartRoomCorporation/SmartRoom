import tkinter as tk
from Sensors.StatusCircle import StatusCircle
from Sensors.ActuatorStatusBar import ActuatorStatusBar

class LightSensor:
    DIMMEROFF = 0
    DIMMERMIDDLE = 50
    DIMMERFULL = 100
    autopilot = True
    actuator = 0
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
    SENSOR = "Light"
    LIGHTUP = "LIGHTUP"
    LIGHTDOWN = "LIGHTDOWN"

    def __init__(self, smartroom):
        self.smartroom = smartroom

    def setGui(self, val):
        self.gui = val

    def setAutoPilot(self, val):
        self.autopilot = val

    def setActuator(self, val):
        self.actuator = val

    def setCurrentValue(self, val):
        self.current_val = val

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
        label=tk.Label(text="Light Sensor",fg="Green",font=("Helevetica",16))
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
        label=tk.Label(left,text="Lumen:",fg="Black",font=("Helevetica",13))
        label.grid(row=2,column=1,padx=5,sticky="W")
        self.curr_output=tk.Label(left,text=self.getCurrentValue(),fg="Black",font=("Helevetica",13),bg="white",bd=1,relief="sunken")
        self.curr_output.grid(row=2,column=2,padx=5,sticky="W")
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
        self.act_status=ActuatorStatusBar(right)
        self.act_status.grid(row=1,column=6,padx=5,pady=5)
        acup_button=tk.Button(right,text="+",command=lambda:self.reqActuatorUp())
        acup_button.grid(row=1,column=7,padx=1)
        acdown_button=tk.Button(right,text="-",command=lambda:self.reqActuatorDown())
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
            self.curr_output.config(text = self.getCurrentValue())
            self.th_output.config(text = self.getThresholdValue())
            if self.getActuator() == self.DIMMERFULL:
                self.act_status.changeStatus(2)
            if self.getActuator() == self.DIMMERMIDDLE:
                self.act_status.changeStatus(1)
            if self.getActuator() == self.DIMMEROFF:
                self.act_status.changeStatus(0)

            self.auto_output.change(self.getAutopilot())

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

    def reqActuatorUp(self):
        data = [self.SENSOR, self.ACTUATOR, self.LIGHTUP]
        command = [self.COMMAND, data]
        self.smartroom.getServerInstance().sendCommand(self.smartroom.getMacAddress(), command)

    def reqActuatorDown(self):
        data = [self.SENSOR, self.ACTUATOR, self.LIGHTDOWN]
        command = [self.COMMAND, data]
        self.smartroom.getServerInstance().sendCommand(self.smartroom.getMacAddress(), command)
