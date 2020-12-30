class LightSensor:
    DIMMEROFF = 0
    DIMMERMIDDLE = 50
    DIMMERFULL = 100
    autopilot = True
    actuator = 0
    current_val = 0
    threshold_val = 0

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