import time
from threading import Thread


class Server(Thread):
    """
    A threading example
    """

    def __init__(self, name, monitor):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self._monitor = monitor

    def run(self):
        """Запуск потока"""
        msg = "%s is running" % self.name
        print(msg)
        self.check()
        msg = "%s is stopped" % self.name
        print(msg)

    def check(self):
        while self._monitor._state == 1:
            print("run")
            time.sleep(self._monitor.get_timeout())
