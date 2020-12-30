import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.modules.SensorModule.TempModule.TempModuleStub import TempModuleStub

class TestTempModule(unittest.TestCase):

    tms = None

    @classmethod
    def setUpClass(cls):
        cls.tms = TempModuleStub()
        cls.tms.setThresholdValue(25)
    
    @classmethod
    def tearDownClass(cls):
        cls.tms = None

    def testCurrentValue(self):
        # lowerboundtest 
        self.tms.setCurrValue(-51)
        self.tms.actuator()
        self.assertEqual(None, self.tms.getActuatorStatus())
        # upperboundtest
        self.tms.setCurrValue(81)
        self.tms.actuator()
        self.assertEqual(None, self.tms.getActuatorStatus())

    def testActuator(self): 
        # testactuatorTrue
        self.tms.setCurrValue(24)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(True, self.tms.getActuatorStatus())
        # testactuatorFalse
        self.tms.setCurrValue(26)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(False, self.tms.getActuatorStatus())

    def testRise(self): # testRISE
        self.tms.setThresholdValue(30)
        self.tms.rise()
        self.assertEqual(30, self.tms.getThresholdValue())
        self.tms.setThresholdValue(29)
        self.tms.rise()
        self.assertEqual(30, self.tms.getThresholdValue())

    def testReduce(self): # testREDUCE
        self.tms.setThresholdValue(18)
        self.tms.reduce()
        self.assertEqual(18, self.tms.getThresholdValue())
        self.tms.setThresholdValue(19)
        self.tms.reduce()
        self.assertEqual(18, self.tms.getThresholdValue())
        
    def testServerCommand(self): # testSERVERCOMMAND
        self.tms.setActuatorStatus(True)
        self.tms.serverCommand("OFF")
        self.assertEqual(False, self.tms.getActuatorStatus())
        self.assertEqual(False, self.tms.getAutopilot())
        self.tms.setThresholdValue(25)
        self.tms.setCurrValue(23)
        self.tms.setReqNumber(12)
        self.tms.setAutoPilot(False)
        self.tms.setActuatorStatus(False)
        self.tms.serverCommand("ON")
        self.assertEqual(True, self.tms.getAutopilot())
        self.tms.actuator()
        self.assertEqual(True, self.tms.getActuatorStatus())

if __name__ == '__main__':
    unittest.main()
