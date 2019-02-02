class DefaultAction:
    """
    Класс по умолчанию для действий над измененными файлами
    Описывает минимальный интерфейс класса
    """
    def __init__(self):
        self._command = "Input file: {0}"

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
        print(cmd)
