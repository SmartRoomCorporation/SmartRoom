import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.modules.SensorModule.AirModule.AirModuleStub import AirModuleStub

class TestAirModule(unittest.TestCase):

    tms = None

    @classmethod
    def setUpClass(cls):
        cls.tms = AirModuleStub()
        cls.tms.setThresholdValue(120)
    
    @classmethod
    def tearDownClass(cls):
        cls.tms = None

    def testCurrentValue(self):
        # lowerboundtest 
        self.tms.setCurrValue(-1)
        self.tms.actuator()
        self.assertEqual(None, self.tms.getActuatorStatus())
        # upperboundtest
        self.tms.setCurrValue(201)
        self.tms.actuator()
        self.assertEqual(None, self.tms.getActuatorStatus())

    def testActuator(self):
        # testactuatorFANOFF
        self.tms.setCurrValue(181)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(0, self.tms.getActuatorStatus())
        # testactuatorFANMIDDLE
        self.tms.setCurrValue(121)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(50, self.tms.getActuatorStatus())
        self.tms.setCurrValue(179)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(50, self.tms.getActuatorStatus())
        # testactuatorFANFULL
        self.tms.setCurrValue(119)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(100, self.tms.getActuatorStatus())

    def testRise(self): # testRISE
        self.tms.setThresholdValue(100)
        self.tms.rise()
        self.assertEqual(120, self.tms.getThresholdValue())
        self.tms.setThresholdValue(180)
        self.tms.rise()
        self.assertEqual(200, self.tms.getThresholdValue())
        self.tms.setThresholdValue(200)
        self.tms.rise()
        self.assertEqual(200, self.tms.getThresholdValue())

    def testReduce(self): # testREDUCE
        self.tms.setThresholdValue(60)
        self.tms.reduce()
        self.assertEqual(40, self.tms.getThresholdValue())
        self.tms.setThresholdValue(20)
        self.tms.reduce()
        self.assertEqual(0, self.tms.getThresholdValue())
        self.tms.setThresholdValue(0)
        self.tms.reduce()
        self.assertEqual(0, self.tms.getThresholdValue())

    def testServerCommand(self): # testSERVERCOMMAND
        self.tms.setAutoPilot(False)
        self.tms.setActuatorStatus(100)
        self.tms.serverCommand("FANUP")
        self.assertEqual(100, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(50)
        self.tms.serverCommand("FANUP")
        self.assertEqual(100, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(0)
        self.tms.serverCommand("FANUP")
        self.assertEqual(50, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(0)
        self.tms.serverCommand("FANDOWN")
        self.assertEqual(0, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(50)
        self.tms.serverCommand("FANDOWN")
        self.assertEqual(0, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(100)
        self.tms.serverCommand("FANDOWN")
        self.assertEqual(50, self.tms.getActuatorStatus())

    def testStartMeasure(self): # testStartMeasure
        self.tms.setCount(0)
        self.assertEqual(80, self.tms.startMeasure())
        self.tms.setCount(15)
        self.tms.setCurrValue(60)
        self.assertEqual(58, self.tms.startMeasure())
        self.tms.setCount(15)
        self.tms.setCurrValue(40)
        self.assertEqual(41, self.tms.startMeasure())
        self.tms.setCount(33)
        self.tms.setCurrValue(85)
        self.assertEqual(90, self.tms.startMeasure())
        self.tms.setCount(33)
        self.tms.setCurrValue(103)
        self.assertEqual(100, self.tms.startMeasure())
        self.tms.setCount(80)
        self.tms.setCurrValue(103)
        self.assertEqual(103, self.tms.startMeasure())

    def testGetCurrentStatus(self): # testGetSensorStatus
        self.tms.setCurrValue(200)
        self.tms.setAutoPilot(False)
        self.tms.setActuatorStatus(50)
        self.tms.setThresholdValue(130)
        self.assertListEqual([200, 130, 50, False], self.tms.getSensorStatus())

if __name__ == '__main__':
    unittest.main()
