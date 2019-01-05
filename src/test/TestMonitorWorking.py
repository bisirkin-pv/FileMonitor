import unittest
from src.monitor.Monitor import Monitor
import time
import os


class TestMonitorWorking(unittest.TestCase):

    def setUp(self):
        self.monitor = Monitor('')
        self.monitor.start()

    # проверяем работоспособность цикла сервера
    def test_working_monitoring(self):

        time.sleep(2)
        self.monitor.set_timeout(2)
        # time.sleep(10)
        execute_code = self.monitor.stop()
        self.assertEqual(0, execute_code)
