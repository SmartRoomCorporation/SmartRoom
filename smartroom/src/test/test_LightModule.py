import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.modules.SensorModule.LightModule.LightModuleStub import LightModuleStub

class TestAirModule(unittest.TestCase):

    tms = None

    @classmethod
    def setUpClass(cls):
        cls.tms = LightModuleStub()
        cls.tms.setThresholdValue(5000)
    
    @classmethod
    def tearDownClass(cls):
        cls.tms = None

    def testCurrentValue(self):
        # lowerboundtest 
        self.tms.setCurrValue(-1)
        self.tms.actuator()
        self.assertEqual(None, self.tms.getActuatorStatus())
        # upperboundtest
        self.tms.setCurrValue(10001)
        self.tms.actuator()
        self.assertEqual(None, self.tms.getActuatorStatus())

    def testActuator(self):
        # testactuatorDIMMEROFF
        self.tms.setCurrValue(7501)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(0, self.tms.getActuatorStatus())
        # testactuatorDIMMERMIDDLE
        self.tms.setCurrValue(5001)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(50, self.tms.getActuatorStatus())
        self.tms.setCurrValue(7499)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(50, self.tms.getActuatorStatus())
        # testactuatorDIMMERFULL
        self.tms.setCurrValue(4999)
        self.tms.setReqNumber(12)
        self.tms.actuator()
        self.assertEqual(100, self.tms.getActuatorStatus())

    def testRise(self): # testRISE
        self.tms.setThresholdValue(10000)
        self.tms.rise()
        self.assertEqual(10000, self.tms.getThresholdValue())
        self.tms.setThresholdValue(9500)
        self.tms.rise()
        self.assertEqual(10000, self.tms.getThresholdValue())

    def testReduce(self): # testREDUCE
        self.tms.setThresholdValue(0)
        self.tms.reduce()
        self.assertEqual(0, self.tms.getThresholdValue())
        self.tms.setThresholdValue(500)
        self.tms.reduce()
        self.assertEqual(0, self.tms.getThresholdValue())

    def testServerCommand(self): # testSERVERCOMMAND
        self.tms.setActuatorStatus(100)
        self.tms.serverCommand("LIGHTUP")
        self.assertEqual(100, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(50)
        self.tms.serverCommand("LIGHTUP")
        self.assertEqual(100, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(0)
        self.tms.serverCommand("LIGHTUP")
        self.assertEqual(50, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(0)
        self.tms.serverCommand("LIGHTDOWN")
        self.assertEqual(0, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(50)
        self.tms.serverCommand("LIGHTDOWN")
        self.assertEqual(0, self.tms.getActuatorStatus())
        self.tms.setActuatorStatus(100)
        self.tms.serverCommand("LIGHTDOWN")
        self.assertEqual(50, self.tms.getActuatorStatus())

if __name__ == '__main__':
    unittest.main()