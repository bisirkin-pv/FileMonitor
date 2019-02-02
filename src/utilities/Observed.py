import itertools


class Observed:
    """
    Класс добавляющий методы для наблюдения
    """
    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        """
        Добавляет наблюдателей и выполняет начальное оповещение
        :param observer:
        :param observers:
        :return:
        """
        for _observer in itertools.chain((observer,), observers):
            self.__observers.add(_observer)
            _observer.update(self)

    def observer_disable(self, observer):
        """
        Отписка от оповещений
        :param observer:
        :return:
        """
        self.__observers.discard(observer)

    def observers_notify(self):
        """
        Оповещение об изменениях
        :return:
        """
        for observer in self.__observers:
            observer.update(self)
