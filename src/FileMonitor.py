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
                        'help': self._print_help,
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
        if self._monitor.get_state() == 0:
            self._monitor.start()
            self._timeout()
        else:
            print("Server is already running")

    def stop_server(self):
        """
        Остановка мониторинга
        :return:
        """
        if self._monitor.get_state() == 1:
            self._monitor.stop()
            self._timeout()
        else:
            print("Server is already stopped")

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
        self.stop_server()

    def _timeout(self):
        """
        Пауза выполенения
        :return:
        """
        time.sleep(self._monitor.get_timeout())

    @staticmethod
    def _print_help():
        """
        Отображает справочную информацию по командам
        :return:
        """
        print("Available command:"
              "\n\tstart - Starting the monitoring server"
              "\n\tstop - Stopping the monitoring server"
              "\n\texit - Exit application"
              )


if __name__ == '__main__':
    file_monitor = FileMonitor(sys.argv[1:])
    file_monitor.run_server()
    file_monitor.wait_input()