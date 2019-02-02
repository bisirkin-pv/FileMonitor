import subprocess
from src.actions.DefaultAction import DefaultAction


class BashAction(DefaultAction):
    """
    Выполняет действия при изменении файла
    Данный класс будет выполнять разные задачи
    """
    def __init__(self, cmd):
        super().__init__()
        self.command = cmd

    def update(self, monitor):
        """
        Текущая задача выполнять генерацию html документации asciidoc
        :return:
        """
        if monitor.value == '':
            return
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
