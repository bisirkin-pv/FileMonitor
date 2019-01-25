class DefaultAction:
    """
    Класс по умолчанию для действий над измененными файлами
    Описывает минимальный интерфейс класса
    """
    def __init__(self):
        self._command = "Input file: {0}"

    def run(self, file):
        """
        Текущая задача выполнять генерацию html документации asciidoc
        :return:
        """
        cmd = self._command.format(file)
        print(cmd)
