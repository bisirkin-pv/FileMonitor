import unittest
from src.monitor.Monitor import Monitor
import os
from src.monitor.Action import Action
from src.monitor.DefaultAction import DefaultAction


class TestMonitorWorking(unittest.TestCase):

    def setUp(self):
        self.monitor = Monitor('^[a-z]+[0-9]+\.txt')
        self.filename_list = ['test.txt', 'test2.txt', 'test3.txt']

    # проверяем разбор пути поиска файлов
    def test_file_parser(self):
        self.create_test_files()
        self.monitor.create_file_list()
        files = self.monitor.get_file_list()
        self.assertEqual(len(files), 2)
        # action = Action()
        # defaultAction = DefaultAction()
        # self.monitor.observers_add(defaultAction, action)
        # self.monitor.refresh()

    def create_test_files(self):
        for name in self.filename_list:
            with open(name, 'w') as file:
                file.write(name)

    def tearDown(self):
        for name in self.filename_list:
            os.remove(name)
