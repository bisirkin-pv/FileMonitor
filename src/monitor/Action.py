import subprocess


class Action:
    """
    Выполняет действия при изменении файла
    Данный класс будет выполнять разные задачи, передавать что делать нужно в файле
    """
    def __init__(self, file):
        self._file = file

    def run(self):
        """
        Текущая задача выполнять генерацию html документации asciidoc
        :return:
        """
        cmd = "asciidoctor -r asciidoctor-diagram -a nofooter {0}".format(self._file)
        subprocess.run(cmd,
                       check=True,
                       shell=True
                       )