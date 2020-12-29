class TempSensor:
    autopilot = True
    actuator = False
    current_val = 0

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