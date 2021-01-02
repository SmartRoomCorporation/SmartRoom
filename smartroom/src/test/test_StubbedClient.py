import unittest
import time
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.SmartRoom import SmartRoom
from main.modules.SensorModule.TempModule.TempModuleStub import TempModuleStub
from main.modules.SensorModule.LightModule.LightModuleStub import LightModuleStub
from main.modules.SensorModule.AirModule.AirModuleStub import AirModuleStub

class TestClient(unittest.TestCase):

    client = None

    @classmethod
    def setup_class(cls):
        cls.client = SmartRoom()
        cls.client.setIp("127.0.0.1")
        tm = TempModuleStub()
        lm = LightModuleStub()
        am = AirModuleStub()
        cls.client.addSensor("Temperature", tm)
        cls.client.addSensor("Light", lm)
        cls.client.addSensor("Air", am)
        cls.client.start()
        time.sleep(2)
        cls.client.sendMessage("TESTAUTOPILOT")
        cls.client.getSensor("Air").setThresholdValue(80)
        cls.client.sendMessage("TESTRISE")
        cls.client.getSensor("Light").setThresholdValue(4000)
        cls.client.sendMessage("TESTREDUCE")
        cls.client.getSensor("Air").setActuatorStatus(50)
        cls.client.sendMessage("TESTCOMMAND")
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        cls.client.sendMessage("STOP")

    def testAutopilotCommand(self):
        self.assertEqual(False, self.client.getSensor("Temperature").getAutopilot())

    def testRiseCommand(self):
        self.assertEqual(100, self.client.getSensor("Air").getThresholdValue())

    def testReduceCommand(self):
        self.assertEqual(3500, self.client.getSensor("Light").getThresholdValue())

    def testServerCommand(self):
        self.assertEqual(100, self.client.getSensor("Air").getActuatorStatus())
    
    
