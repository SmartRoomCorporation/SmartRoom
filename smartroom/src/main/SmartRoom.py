class SmartRoom:
    sensors = dict()

    def addSensor(self, sensor, sensorobj):
        self.sensors[sensor] = sensorobj

    def getSensor(self, sensor):
        if(sensor in self.sensors): return self.sensors.get(sensor)
        return False

    def getSensorsList(self):
        return self.sensors
