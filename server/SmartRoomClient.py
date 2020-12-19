class SmartRoomClient:
    macaddress = ""
    sensors = dict()

    def setMacAddress(self, macaddr):
        self.macaddress = macaddr

    def updateSensors(self, sensors):
        self.sensors = sensors

    def getSensorValue(self, sensor):
        if(sensor in self.sensors): return self.sensors.get(sensor)
        return False

    def getSensorsList(self):
        return self.sensors
