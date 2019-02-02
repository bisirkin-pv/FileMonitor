import subprocess
from src.actions.DefaultAction import DefaultAction


class AsciiDocGenerateHtmlAction(DefaultAction):
    """
    Выполняет действия при изменении файла
    Данный класс будет выполнять разные задачи
    """
    def __init__(self):
        super().__init__()
        self.command = "asciidoctor -r asciidoctor-diagram -a nofooter -a linkcss {0}"

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
