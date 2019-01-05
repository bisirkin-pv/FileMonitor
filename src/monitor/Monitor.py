import time
from src.monitor.Server import Server


class Monitor:
    """
    Класс осуществляет наблюдение за изменениями файлов
    """
    def __init__(self):
        self._state = 0     # состояние сервера  (1 - запущен, 0 - остановлен, другое - ошибка)
        self._timeout = 5  # таймаут между итерациями (секунд)

    def start(self):
        """
        Запускает наблюдение за файлами
        :return:
        """
        self._state = 1 if self._state == 0 else self._state
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
        :return: _state (int)
        """
        return self._state

    def get_timeout(self):
        """
        Возвращает текущий таймаут выполения
        :return: timeout (int) second
        """
        return self._timeout

    def set_timeout(self, sec):
        """
        Устанавливает таймаут
        :param sec: (int) second
        :return:
        """
        self._timeout = sec

