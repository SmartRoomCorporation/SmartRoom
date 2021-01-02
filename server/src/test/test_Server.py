import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.Server import SmartroomServer
from main.SmartRoomClient import SmartRoomClient
import json
from pprint import pprint

class TestServer(unittest.TestCase):

    server = None
    sr = None

    @classmethod
    def setUpClass(cls):
        cls.server = SmartroomServer()
        cls.sr = SmartRoomClient(cls.server)
        clientTopic = "STUBTOPIC"
        cls.sr.setMacAddress(clientTopic)
        cls.server.addSmartRoomClient(clientTopic, cls.sr)
    
    @classmethod
    def tearDownClass(cls):
        cls.server = None

    def testSensorsListRequest(self):
        d = ["SENSORSLIST", {'Temperature': [15, 25, False, True], 'Light': [1500, 5000, 0, True], 'Air': [80, 100, 0, True]}]
        self.server.decodeMessage("STUBTOPIC-server", d)
        sr = self.server.getSmartRoomClient("STUBTOPIC")
        sensor = sr.getSensor("Temperature")
        self.assertEqual(15, sensor.getCurrentValue())
        self.assertEqual(25, sensor.getThresholdValue())
        self.assertEqual(False, sensor.getActuator())
        self.assertEqual(True, sensor.getAutopilot())
        sensor = sr.getSensor("Light")
        self.assertEqual(1500, sensor.getCurrentValue())
        self.assertEqual(5000, sensor.getThresholdValue())
        self.assertEqual(0, sensor.getActuator())
        self.assertEqual(True, sensor.getAutopilot())
        sensor = sr.getSensor("Air")
        self.assertEqual(80, sensor.getCurrentValue())
        self.assertEqual(100, sensor.getThresholdValue())
        self.assertEqual(0, sensor.getActuator())
        self.assertEqual(True, sensor.getAutopilot())

    def testUpdateSensorRequest(self):
        d = ["SENSORSLIST", {'Temperature': [15, 25, False, True], 'Light': [1500, 5000, 0, True], 'Air': [80, 100, 0, True]}]
        self.server.decodeMessage("STUBTOPIC-server", d)
        sr = self.server.getSmartRoomClient("STUBTOPIC")
        sensor = sr.getSensor("Air")
        self.assertEqual(80, sensor.getCurrentValue())
        self.assertEqual(0, sensor.getActuator())
        self.assertEqual(True, sensor.getAutopilot())
        d = ["UPDATESENSOR", {'Air': [7000, 5000, 50, False]}]
        self.server.decodeMessage("STUBTOPIC-server", d)
        sr = self.server.getSmartRoomClient("STUBTOPIC")
        sensor = sr.getSensor("Air")
        self.assertEqual(7000, sensor.getCurrentValue())
        self.assertEqual(5000, sensor.getThresholdValue())
        self.assertEqual(50, sensor.getActuator())
        self.assertEqual(False, sensor.getAutopilot())

if __name__ == '__main__':
    unittest.main()