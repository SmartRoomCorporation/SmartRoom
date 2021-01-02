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
        self.tms.setThresholdValue(20)
        self.tms.rise()
        self.assertEqual(21, self.tms.getThresholdValue())

    def testReduce(self): # testREDUCE
        self.tms.setThresholdValue(18)
        self.tms.reduce()
        self.assertEqual(18, self.tms.getThresholdValue())
        self.tms.setThresholdValue(19)
        self.tms.reduce()
        self.assertEqual(18, self.tms.getThresholdValue())
        self.tms.setThresholdValue(20)
        self.tms.reduce()
        self.assertEqual(19, self.tms.getThresholdValue())

    def testServerCommand(self): # testSERVERCOMMAND
        self.tms.setAutoPilot(False)
        self.tms.setActuatorStatus(True)
        self.tms.serverCommand("OFF")
        self.assertEqual(False, self.tms.getActuatorStatus())
        self.assertEqual(False, self.tms.getAutoPilot())
        self.tms.setThresholdValue(25)
        self.tms.setCurrValue(23)
        self.tms.setReqNumber(12)
        self.tms.setAutoPilot(False)
        self.tms.setActuatorStatus(False)
        self.tms.serverCommand("ON")
        self.assertEqual(True, self.tms.getAutoPilot())
        self.tms.actuator()
        self.assertEqual(True, self.tms.getActuatorStatus())

    def testStartMeasure(self): #testSTARTMEASURE
        self.tms.setCount(0)
        self.tms.startMeasure()
        self.assertEqual(15, self.tms.getCurrValue())
        self.assertEqual(1, self.tms.getCount())
        self.tms.setCount(3)
        self.tms.startMeasure()
        self.assertEqual(14, self.tms.getCurrValue())
        self.tms.setCurrValue(9)
        self.tms.setCount(3)
        self.tms.startMeasure()
        self.assertEqual(10, self.tms.getCurrValue())
        self.tms.setCurrValue(20)
        self.tms.setCount(33)
        self.tms.startMeasure()
        self.assertEqual(19, self.tms.getCurrValue())
        self.tms.setCurrValue(29)
        self.tms.setCount(33)
        self.tms.startMeasure()
        self.assertEqual(30, self.tms.getCurrValue())
        self.tms.setCurrValue(20)
        self.tms.setCount(71)
        self.tms.startMeasure()
        self.assertEqual(20, self.tms.getCurrValue())

    def testGetSensorStatus(self): #testGETSENSORSTATUS
        self.tms.setCurrValue(20)
        self.tms.setAutoPilot(True)
        self.tms.setActuatorStatus(True)
        self.tms.setThresholdValue(19)
        self.assertListEqual([20, 19, True, True], self.tms.getSensorStatus())


if __name__ == '__main__':
    unittest.main()
