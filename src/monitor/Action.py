import subprocess


class Action:
    """
    Выполняет действия при изменении файла
    Данный класс будет выполнять разные задачи
    """
    def __init__(self):
        self._command = "asciidoctor -r asciidoctor-diagram -a nofooter -a linkcss {0}"

    def set_command(self, cmd):
        """
        Устанавливает команду для выполнения
        :param cmd:
        :return:
        """
        self._command = cmd

    def get_command(self):
        """
        Команда для выполнения
        :return:
        """
        return self._command

    def run(self, file):
        """
        Текущая задача выполнять генерацию html документации asciidoc
        :return:
        """
        cmd = self._command.format(file)
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
