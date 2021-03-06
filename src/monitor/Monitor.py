import time
from src.monitor.Server import Server
import re
from src.monitor.FileProperty import FileProperty
import os
from pathlib import Path
from src.utilities.Observed import Observed


class Monitor(Observed):
    """
    Класс осуществляет наблюдение за изменениями файлов
    """
    def __init__(self, re_files):
        super().__init__()
        self._state = 0               # состояние сервера  (1 - запущен, 0 - остановлен, другое - ошибка)
        self._timeout = 5             # таймаут между итерациями (секунд)
        self._re_files = re_files     # регулярное выражение поиска файлов
        self._files = []              # список параметров файлов
        self.__change_file_name = ""  # Имя измененного файла
        self.value = ""

    @property
    def value(self):
        return self.__change_file_name

    @value.setter
    def value(self, value):
        self.__change_file_name = value
        self.observers_notify()

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
        self._files = []
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
        """
        Проверка на соответствие регулярному выражению
        :param file: название файла
        :param reg: регулярное выражение
        :return: 1- совпадение найдено иначе 0
        """
        pattern = re.compile(reg)
        return 1 if pattern.search(file) is not None else 0

    def check(self):
        """
        Производит проверку на изменение файла
        :return:
        """
        for i in range(len(self._files)):
            full_name = os.path.join(self._files[i].path, self._files[i].name)
            changed = time.ctime(os.path.getmtime(full_name))
            if changed != self._files[i].change_date:
                self.value = full_name
                self._files[i] = FileProperty(self._files[i].path,
                                              self._files[i].name,
                                              changed
                                              )

    def refresh(self):
        """
        Принудительное выполнение команды для всех файлов
        :return:
        """
        self.create_file_list()
        for i in range(len(self._files)):
            self.value = os.path.join(self._files[i].path, self._files[i].name)
