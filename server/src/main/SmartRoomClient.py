from Sensors.AirSensor import AirSensor
from Sensors.TempSensor import TempSensor
from Sensors.LightSensor import LightSensor
from pprint import pprint

class SmartRoomClient:
    macaddress = ""
    sensors = dict()
    connected = True
    TEMPERATURE = "Temperature"
    AIR = "Air"
    LIGHT = "Light"
    server_instance = ""
    active = False

    def __init__(self, server):
        self.server_instance = server

    def getServerInstance(self):
        return self.server_instance

    def setActive(self, val):
        self.active = val

    def getActive(self):
        return self.active

    def setMacAddress(self, macaddr):
        self.macaddress = macaddr

    def getMacAddress(self):
        return self.macaddress

    def updateSensors(self, sensors):
        self.sensors = sensors

    def getSensor(self, sensor):
        if(sensor in self.sensors): return self.sensors.get(sensor)
        return False

    def addSensor(self, sensor, data):
        s = None
        if(sensor == self.TEMPERATURE):
            s = TempSensor(self)
        elif(sensor == self.AIR):
            s = AirSensor(self)
        elif(sensor == self.LIGHT):
            s = LightSensor(self)
        else: return False # TODO RAISE EXCEPTION
        s.setCurrentValue(data[0])
        s.setThresholdValue(data[1])
        s.setActuator(data[2])
        s.setAutoPilot(data[3])
        self.sensors[sensor] = s

    def updateSensor(self, sensor, data):
        if(sensor in self.sensors):
            self.sensors[sensor].setCurrentValue(data[0])
            self.sensors[sensor].setThresholdValue(data[1])
            self.sensors[sensor].setActuator(data[2])
            self.sensors[sensor].setAutoPilot(data[3])
            self.sensors[sensor].updateGui()
        else: return False # TODO RAISE EXCEPTION

    def isConnected(self):
        return self.connected

    def setConnected(self, val):
        self.connected = val

    def getSensorsList(self):
        return self.sensors
