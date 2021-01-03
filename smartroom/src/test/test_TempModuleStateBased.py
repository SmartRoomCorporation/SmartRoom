import unittest
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from main.modules.SensorModule.TempModule.TempModuleStub import TempModuleStub

class TestTempModuleStateBased(unittest.TestCase):
    tms = None

    @classmethod
    def setUp(cls):
        cls.tms = TempModuleStub() # s0

    @classmethod
    def tearDown(cls):
        cls.tms = None

    def testDriverS4(self):
        self.tms.manualCommand(False) # s1
        self.tms.startMeasure() # s5
        self.tms.setCount(31) # s6
        self.tms.setCount(75) # s7
        self.tms.serverCommand("ON") # s4
        # s4 assertions
        self.assertGreater(self.tms.count, 70)
        self.assertEqual(self.tms.actuator_status, False)
        self.assertEqual(self.tms.autopilot, True)
        
    def testDriverS7(self):
        self.tms.startMeasure() # s2
        while(self.tms.getReqNumber() < self.tms.MAXREQNUMBER): self.tms.actuator() # s9
        self.tms.actuator()
        self.tms.setCount(32) # s10
        self.tms.setCount(75) # s11
        self.tms.manualCommand(False) # s7
        # s7 assertions
        self.assertGreater(self.tms.count, 70)
        self.assertEqual(self.tms.actuator_status, False)
        self.assertEqual(self.tms.autopilot, False)

    def testDriverS9(self):
        self.tms.setCount(71) # s4
        self.tms.startMeasure() # s2
        while(self.tms.getReqNumber() < self.tms.MAXREQNUMBER): self.tms.actuator() # s9
        self.tms.actuator()
        self.tms.manualCommand(False) # s5
        self.tms.setCount(54) # s6
        self.tms.serverCommand("ON") # s3
        while(self.tms.getReqNumber() < self.tms.MAXREQNUMBER): self.tms.actuator() # s10
        self.tms.actuator()
        self.tms.setCount(71) # s11
        self.tms.startMeasure() # s9
        # s9 assertions
        self.assertGreater(self.tms.count, 0)
        self.assertLess(self.tms.count, 20)
        self.assertEqual(self.tms.actuator_status, True)
        self.assertEqual(self.tms.autopilot, True)

    def testDriverS6(self):
        self.tms.manualCommand(False) # s1
        self.tms.startMeasure() # s5
        self.tms.setCount(44) # s6
        while(self.tms.getCount() < 60): self.tms.startMeasure() # s6
        # s6 assertions
        self.assertGreater(self.tms.count, 30)
        self.assertLessEqual(self.tms.count, 60)
        self.assertEqual(self.tms.actuator_status, False)
        self.assertEqual(self.tms.autopilot, False)    


if __name__ == '__main__':
    unittest.main()