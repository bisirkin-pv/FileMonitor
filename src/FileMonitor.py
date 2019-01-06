from src.monitor.Monitor import Monitor
import sys
import argparse
import time

class FileMonitor:
    """
    Класс запуска мониторинга
    """
    def __init__(self, args):
        """
        Принимает список параметров
        :param args:
        """
        self._args = args
        self._namespace = {}
        self._param_parser()
        self._monitor = Monitor(self._namespace.re_path)
        self._isWait = True
        self._command = {
                        'stop': self.stop_server,
                        'start': self.run_server,
                        'exit': self._stop_wait,
                        }

    def _param_parser(self):
        """
        Разбор входных параметров
        :return:
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('-p', '--re_path', default='')
        self._namespace = parser.parse_args(self._args)

    def run_server(self):
        """
        Запуск мониторинга
        :return:
        """
        self._monitor.start()

    def stop_server(self):
        """
        Остановка мониторинга
        :return:
        """
        self._monitor.stop()
        time.sleep(self._monitor.get_timeout())

    def wait_input(self):
        """
        Ожидание ввода команды в CLI
        :return:
        """
        while self._isWait:
            command = input(">>")
            try:
                self._command.get(command.strip())()
            except TypeError:
                print("Command not found. Type 'help' for more info")

    def _stop_wait(self):
        """
        Остановка сервиса
        :return:
        """
        self._isWait = False
        if self._monitor.get_state() == 1:
            self.stop_server()


if __name__ == '__main__':
    file_monitor = FileMonitor(sys.argv[1:])
    file_monitor.run_server()
    print("start")
    file_monitor.wait_input()