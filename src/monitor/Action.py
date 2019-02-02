import subprocess


class Action:
    """
    Выполняет действия при изменении файла
    Данный класс будет выполнять разные задачи
    """
    def __init__(self):
        self._command = None
        self.command = "asciidoctor -r asciidoctor-diagram -a nofooter -a linkcss {0}"

    @property
    def command(self):
        """
        Команда для выполнения
        :return:
        """
        return self._command

    @command.setter
    def command(self, cmd):
        """
        Устанавливает команду для выполнения
        :param cmd:
        :return:
        """
        self._command = cmd

    def update(self, monitor):
        """
        Текущая задача выполнять генерацию html документации asciidoc
        :return:
        """
        cmd = self.command.format(monitor.value)
        try:
            subprocess.run(cmd,
                           check=True,
                           shell=True,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE
                           )
        except subprocess.CalledProcessError as e:
            print(e)
