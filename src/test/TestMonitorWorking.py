import unittest
from src.monitor.Monitor import Monitor
import time


class TestMonitorWorking(unittest.TestCase):

    def setUp(self):
        self.monitor = Monitor('')
        self.monitor.start()

    # проверяем работоспособность цикла сервера
    def test_working_monitoring(self):
        state = self.monitor.get_state()
        self.assertEqual(state.get('state'), 1)
        self.assertGreater(state.get('file_count'), -1)
        time.sleep(2)
        self.monitor.set_timeout(2)
        # time.sleep(10)
        execute_code = self.monitor.stop()
        self.assertEqual(0, execute_code)
