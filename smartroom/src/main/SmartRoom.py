import paho.mqtt.client as mqtt
from uuid import getnode as get_mac
import json
from threading import Thread
from modules.SensorModule.TempModule.TempHumModule import TempHumModule
from modules.SensorModule.LightModule.LightModule import LightModule
from modules.SensorModule.AirModule.AirModuleStub import AirModuleStub
import logging

logging.basicConfig(filename='log.log')
log = logging.getLogger("MQTT_LOG_DEBUG")
topic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))
serverTopic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))+'-server' # output from client
DATAMSG = "DATAMSG"
LIGHTMODULE = "LIGHTMODULE"
TEMPHUMMODULE = "TEMPHUMMODULE"
AIRMODULE = "AIRMODULE"
HUMMODULE = "HUMMODULE"
GETSTATUS = "GETSTATUS"
SENSORSLIST = "SENSORSLIST"
UPDATESENSOR = "UPDATESENSOR"
COMMAND = "COMMAND"
RISE = "RISE"
REDUCE = "REDUCE"
AUTOON = "AUTOON"
AUTOOFF = "AUTOOFF"
ACTUATOR = "ACTUATOR"
SUBSCRIBED = "SUBSCRIBED"
SENSORSSTATUS = "SENSORSSTATUS"
SENSORSTATUS = "SENSORSTATUS"
SENSORREG = "SENSORREG"
SENSORSUB = "SENSORSUB"
CONFIRMSUB = "CONFIRMSUB"
CONFIRMREG = "CONFIRMREG"

class SmartRoom(Thread):
    sensors = dict()
    client = mqtt.Client()
    ip = "127.0.0.1"
    port = 1883
    camera = None
    ttl = 60
    configFile = "smartroom.conf"
    gui = None
    logFile = None

    def setGui(self, realGui):
        self.gui = realGui

    def setPort(self, port):
        self.port = port

    def setTtl(self, ttl):
        self.ttl = ttl

    def setIp(self, ip):
        self.ip = ip

    def setCamera(self, camera):
        self.camera = camera

    def getCamera(self):
        return self.camera

    def checkIsRegistered(self, sensor):
        for key, value in self.sensors.items():
            if(value.getMac() == sensor): return True
        return False

    def createLightSensor(self, sensor):
        lm = LightModule()
        lm.setType(sensor['type'])
        lm.setName(sensor['name'])
        lm.setMac(sensor['mac'])
        lm.setSmartroom(self)
        lm.switchConnectionStatus()
        self.addSensor("Light", lm)
        self.client.publish(sensor['mac'] + "-SUB", json.dumps((CONFIRMREG)), qos=0, retain=False)
        lm.setActuatorStatus(0)
        self.gui.initSensor(lm)

    def createTempHumSensor(self, sensor):
        tm = TempHumModule()
        tm.setType(sensor['type'])
        tm.setName(sensor['name'])
        tm.setMac(sensor['mac'])
        tm.setSmartroom(self)
        tm.switchConnectionStatus()
        self.addSensor("Temperature", tm)
        self.client.publish(sensor['mac'] + "-SUB", json.dumps((CONFIRMREG)), qos=0, retain=False)
        tm.setActuatorStatus("OFF")
        self.gui.initSensor(tm)

    def createAirModule(self, sensor):
        am = AirModuleStub()
        am.setType(sensor['type'])
        am.setName(sensor['name'])
        am.setMac(sensor['mac'])
        am.setSmartroom(self)
        am.switchConnectionStatus()
        am.switchConnectionStatus()
        self.addSensor("Air", am)
        self.client.publish(sensor['mac'] + "-SUB", json.dumps((CONFIRMREG)), qos=0, retain=False)
        am.setActuatorStatus(0)
        self.gui.initSensor(am)

    def createSensor(self, sensor):
        if(self.checkIsRegistered(sensor['mac'])): return False
        if(sensor['type'] == LIGHTMODULE):
            self.createLightSensor(sensor)
        elif(sensor['type'] == AIRMODULE):
            self.createAirModule(sensor)
        elif(sensor['type'] == TEMPHUMMODULE):
            self.createTempHumSensor(sensor)

    def addSensor(self, sensor, sensorobj):
        self.sensors[sensor] = sensorobj

    def getSensor(self, sensor):
        if(sensor in self.sensors): return self.sensors.get(sensor)
        return False

    def getSensorsList(self):
        return self.sensors
    
    def initClient(self):
        if(self.ip is not None):
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.on_publish = self.on_publish
            self.client.enable_logger(logger=log)
            self.client.on_log = self.on_log
            self.client.connect_async(self.ip, self.port, self.ttl)
            self.initLogFile()
            self.client.loop_start()
    
    def checkSensorFromList(self, sensor):
        f = open("sensorlist.txt", "r")
        lines = f.readlines()
        for line in lines:
            if(line.strip() == sensor): 
                logging.debug("+++++++++++++++++++++")
                logging.debug(sensor + " added")
                logging.debug("+++++++++++++++++++++")
                return True
        return False

    def subscribeSingleSensor(self, sensor):
        self.client.subscribe(sensor + "-PUB")

    def trySub(self, sensor):
        if(self.checkIsRegistered(sensor)): return False
        if(self.checkSensorFromList(sensor)): 
            self.subscribeSingleSensor(sensor)
            return True
        return False

    def getRoomStatus(self):
        currStatus = dict()
        for key, value in self.sensors.items():
            currVal = value.startMeasure()
            value.actuator()
            currTh = value.getThresholdValue()
            currAct = value.getActuatorStatus()
            autopilot = value.getAutoPilot()
            currStatus[key] = (currVal, currTh, currAct, autopilot)
        return currStatus

    def on_connect(self, client, userdata, flags, rc): # on connect callback
        client.subscribe(str(topic))
        client.subscribe(str(SENSORSUB))
        client.publish("subreqq", topic, qos=0, retain=False)

    def on_message(self, client, userdata, msg): # on message callback
        if(msg.topic == topic):
            self.decodeMessage(json.loads(str(msg.payload.decode("utf-8"))))
        elif(msg.topic == SENSORSUB):
            sens = str(msg.payload.decode("utf-8"))
            if(self.trySub(sens)):
                client.publish(str(sens) + "-SUB", json.dumps((CONFIRMSUB)), qos=0, retain=False)
        else:
            self.decodeSensorMessage(json.loads(str(msg.payload.decode("utf-8"))))

    def updateReq(self, sensor, data):
        data = {sensor : data}
        self.client.publish(serverTopic, json.dumps((UPDATESENSOR, data)), qos=0, retain=False)

    def on_publish(self, client, userdata, mid): # on publish callback
        return True

    def on_log(self, client, userdata, level, buf):
        self.logMe(buf + "\n")

    def pubToServ(self):
        return self.getRoomStatus()

    def sendMessage(self, message):
        self.client.publish(serverTopic, message, qos=0, retain=False)

    def sendSensorsStatus(self):
        data = dict()
        for key, value in self.sensors.items():
            data[key] = value.getSensorStatus()
        self.client.publish(serverTopic, json.dumps((UPDATESENSOR, data)), qos=0, retain=False)

    def requestSensorStatus(self, sensor):
        topic = sensor.getMac();
        self.client.publish(topic + "-SUB", GETSTATUS, qos=0, retain=False)

    def run(self):
        self.initClient()

    def stopClient(self):
        self.client.loop_stop()
        self.client.disconnect()

    def decodeSensorMessage(self, payload):
        if(payload["msgType"] == "SENSORREG"):
            #print(payload)
            self.createSensor(payload)
        if(payload["msgType"] == "DATAMSG"):
            #print(payload)
            self.decodeMeasure(payload)

    def decodeMeasure(self, payload):
        if(payload["type"] == LIGHTMODULE):
            for key, value in self.sensors.items():
                if(value.getType() == LIGHTMODULE and value.getMac() == payload["mac"]):
                    value.readMeasures(payload["data"])
        elif(payload["type"] == TEMPHUMMODULE):
            for key, value in self.sensors.items():
                if(value.getType() == TEMPHUMMODULE and value.getMac() == payload["mac"]):
                    value.readMeasures(payload["data"])

    def decodeMessage(self, request):
        #print(request)
        if(request == GETSTATUS):
            #print(json.dumps((SENSORSLIST, self.getRoomStatus())))
            self.client.publish(serverTopic, json.dumps((SENSORSLIST, self.getRoomStatus())), qos=0, retain=False)
            return False
        if(request == SENSORSSTATUS):
            self.sendSensorsStatus()
            return False
        try:
            data = request.pop()
            request = request[0]
        except:
            return False
        if(request == SUBSCRIBED): print("Subscribed on " + data)
        if(request == COMMAND):
            sensor = self.getSensor(data[0])
            command = data[1]
            if(command == RISE): sensor.rise()
            if(command == REDUCE): sensor.reduce()
            if(command == AUTOON): sensor.setAutoPilot(True)
            if(command == AUTOOFF): sensor.setAutoPilot(False)
            if(command == ACTUATOR): sensor.serverCommand(data[2])
            self.updateReq(data[0], sensor.getSensorStatus())
    
    def sendDirectCommand(self, topic, command):
        #print(json.dumps(command))
        self.client.publish(topic + "-SUB", json.dumps(command), qos=0, retain=False)

    def logMe(self, msg):
        self.logFile = open("log.log", "a")
        self.logFile.write(msg)
        self.logFile.close()

    def initLogFile(self):
        self.logFile = open("log.log", "w")
        self.logFile.write("")
        self.logFile.close()