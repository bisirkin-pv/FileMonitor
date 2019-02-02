from src.monitor.Monitor import Monitor
import sys
import argparse
import time
import os
from src.actions.AsciiDocGenerateHtmlAction import AsciiDocGenerateHtmlAction


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
                        'state': self.state_server,
                        'list': self.monitoring_file_list,
                        'exit': self._stop_wait,
                        'help': self._print_help,
                        'refresh': self.refresh,
                        'set_command': self.set_action_command,
                        'command': self.get_action_command,
                        'set_timeout': self.set_timeout,
                        'timeout': self.get_timeout,
                        }
        self._action = AsciiDocGenerateHtmlAction()  # Обрабатываемое событие

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
        if self._monitor.get_state().get('state') == 0:
            self._monitor.observers_add(self._action)
            self._monitor.start()
            self._timeout()
        else:
            print("Server is already running")

    def stop_server(self):
        """
        Остановка мониторинга
        :return:
        """
        if self._monitor.get_state().get('state') == 1:
            self._monitor.stop()
            self._monitor.observer_disable(self._action)
            self._timeout()
        else:
            print("Server is already stopped")

    def state_server(self):
        """
        Отображает информацию по состоянию сервера
        :return:
        """
        state = self._monitor.get_state()
        print("State: {0}\nWatch: {1} file(s)".format(
                  'active' if state.get('state') == 1 else 'inactive',
                  state.get('file_count')
                  )
              )

    def monitoring_file_list(self):
        """
        Отображает список файлов под наблюдением
        :return:
        """
        for file in self._monitor.get_file_list():
            print("Filename: {0}".format(os.path.join(file.path, file.name)))

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

    def refresh(self):
        """
        Выполнение команды для всех файлов
        :return:
        """
        self._monitor.refresh()

    def set_action_command(self):
        """
        Команда для выполенения
        !!! Является не безопасной, использовать только локально
        :param cmd: команда для bash
        :return:
        """
        cmd = input("Input command:")
        self._action.command = cmd

    def get_action_command(self):
        """
        Отображает текущую комманду
        :return:
        """
        print("Current command: {}".format(self._action.command))

    def set_timeout(self):
        """
        Устанавливает таймаут опроса изменения файлов
        :param sec: секунды задержки(должны быть больше 0)
        :return:
        """
        try:
            sec = int(input("Input seconds:"))
            if sec > 0:
                self._monitor.set_timeout(sec)
        except ValueError as e:
            print("Value mast by integer")

    def get_timeout(self):
        print("Current timeout: {}".format(self._monitor.get_timeout()))

    @staticmethod
    def _print_help():
        """
        Отображает справочную информацию по командам
        :return:
        """
        print("Available command:"
              "\n\tstart        - Starting the monitoring server"
              "\n\tstop         - Stopping the monitoring server"
              "\n\tstate        - Current state and count of monitored files"
              "\n\tlist         - List of monitored files"
              "\n\trefresh      - Apply the command to all files"
              "\n\tcommand      - Current command"
              "\n\tset_command  - Apply the command"
              "\n\tset_timeout  - Apply check timeout"
              "\n\ttimeout      - Current timeout"
              "\n\texit         - Exit application"
              )


if __name__ == '__main__':
    file_monitor = FileMonitor(sys.argv[1:])
    file_monitor.run_server()
    file_monitor.wait_input()
