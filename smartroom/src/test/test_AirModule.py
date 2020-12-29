import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.modules.SensorModule.AirModule.AirModuleStub import AirModuleStub



class TestAirModule(unittest.TestCase):

    def testCurrentValue(self):
        tms = AirModuleStub(None)
        tms.setThresholdValue(120)
        # lowerboundtest 
        tms.setCurrValue(-1)
        tms.actuator()
        self.assertEqual(None, tms.getActuatorStatus())
        # upperboundtest
        tms.setCurrValue(201)
        tms.actuator()
        self.assertEqual(None, tms.getActuatorStatus())
        # testactuatorFANOFF
        tms.setCurrValue(181)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(0, tms.getActuatorStatus())
        # testactuatorFANMIDDLE
        tms.setCurrValue(121)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(50, tms.getActuatorStatus())
        tms.setCurrValue(179)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(50, tms.getActuatorStatus())
        # testactuatorFANFULL
        tms.setCurrValue(119)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(100, tms.getActuatorStatus())
