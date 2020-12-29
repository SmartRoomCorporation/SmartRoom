import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.modules.SensorModule.LightModule.LightModuleStub import LightModuleStub



class TestAirModule(unittest.TestCase):

    def testCurrentValue(self):
        tms = LightModuleStub()
        tms.setThresholdValue(5000)
        # lowerboundtest 
        tms.setCurrValue(-1)
        tms.actuator()
        self.assertEqual(None, tms.getActuatorStatus())
        # upperboundtest
        tms.setCurrValue(10001)
        tms.actuator()
        self.assertEqual(None, tms.getActuatorStatus())
        # testactuatorDIMMEROFF
        tms.setCurrValue(7501)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(0, tms.getActuatorStatus())
        # testactuatorDIMMERMIDDLE
        tms.setCurrValue(5001)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(50, tms.getActuatorStatus())
        tms.setCurrValue(7499)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(50, tms.getActuatorStatus())
        # testactuatorDIMMERFULL
        tms.setCurrValue(4999)
        tms.setReqNumber(12)
        tms.actuator()
        self.assertEqual(100, tms.getActuatorStatus())

if __name__ == '__main__':
    unittest.main()