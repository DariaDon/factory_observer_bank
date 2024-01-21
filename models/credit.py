from .observable import Observable
from patterns.observer import Observer

class Credit(Observable):
    """Заявка на кредит"""
    
    def __init__(self):
        """Состояние заявки"""
        self.__state = None
        """Список наблюдателей за заявкой"""
        self.__observers: list[Observer] = []

    def update(self, state: str):
        """Изменение состояния заявки"""
        self.__state = state
        self.notify()

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        """Отправить уведомления всем наблюдателям"""
        for observer in self.__observers:
            observer.update(f'по заявке принято решение: {self.__state}')
