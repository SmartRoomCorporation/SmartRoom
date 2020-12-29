import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.modules.SensorModule.TempModule.TempModuleStub import TempModuleStub



class TestTempModule(unittest.TestCase):

    def testCurrentValue(self):
        tms = TempModuleStub()
        tms.setThresholdValue(25)
        # lowerboundtest 
        tms.setCurrValue(-51)
        tms.actuator()
        self.assertEqual(None, tms.getActuatorStatus())
        # upperboundtest
        tms.setCurrValue(81)
        tms.actuator()
        self.assertEqual(None, tms.getActuatorStatus())
        # testactuatorTrue
        tms.setCurrValue(24)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(True, tms.getActuatorStatus())
        # testactuatorFalse
        tms.setCurrValue(26)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(False, tms.getActuatorStatus())
