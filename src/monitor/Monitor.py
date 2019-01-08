import time
from src.monitor.Server import Server
import re
from src.monitor.FileProperty import FileProperty
import os
from pathlib import Path
import datetime


class Monitor:
    """
    Класс осуществляет наблюдение за изменениями файлов
    """
    def __init__(self, re_files):
        self._state = 0             # состояние сервера  (1 - запущен, 0 - остановлен, другое - ошибка)
        self._timeout = 5           # таймаут между итерациями (секунд)
        self._re_files = re_files   # регулярное выражение поиска файлов
        self._files = []            # список параметров файлов

    def start(self):
        """
        Запускает наблюдение за файлами
        :return:
        """
        self._state = 1 if self._state == 0 else self._state
        self.create_file_list()
        server = Server("FileMonitor", self).start()

    def stop(self):
        """
        Останавливает наблюдение за файлами
        :return: execution_code (int)
        """
        self._state = 0 if self._state == 1 else self._state
        return 0 if self._state == 0 else self._state

    def get_state(self):
        """
        Возвращает текущее состояние сервера
        :return: {state: int, file_count: int}
        """
        return dict(state=self._state, file_count=len(self._files))

    def get_timeout(self):
        """
        Возвращает текущий таймаут выполения
        :return: timeout (int) second
        """
        return self._timeout

    def get_file_list(self):
        """
        Возвращает список наблюдаемых файлов
        :return:
        """
        return self._files

    def set_timeout(self, sec):
        """
        Устанавливает таймаут
        :param sec: (int) second
        :return:
        """
        self._timeout = sec

    def create_file_list(self):
        """
        Наполняем список наблюдаемых файлов
        :return:
        """
        path, extension = os.path.split(self._re_files)
        home = str(Path.home())
        path = path.replace('~', home)
        path = path if path != '' else os.getcwd()
        for root, dirs, files in os.walk(path):
            for file in files:
                if self.filter_file(file, extension) == 1:
                    file_property = FileProperty(root, file, time.ctime(os.path.getmtime(os.path.join(root, file))))
                    self._files.append(file_property)

    @staticmethod
    def filter_file(file, reg):
        pattern = re.compile(reg)
        return 1 if pattern.match(file) is not None else 0


