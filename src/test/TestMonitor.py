import unittest
from src.monitor.Monitor import Monitor
import time


class TestMonitor(unittest.TestCase):

    def setUp(self):
        self.monitor = Monitor()
        self.monitor.start()

    def test_stop_monitoring(self):
        print(self.monitor.get_state())
        time.sleep(2)
        self.monitor.set_timeout(2)
        time.sleep(10)
        execute_code = self.monitor.stop()
        self.assertEqual(0, execute_code)
