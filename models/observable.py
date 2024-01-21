from abc import ABC, abstractmethod

class Observable(ABC):
    """Абстрактный объект наблюдения"""

    @abstractmethod    
    def attach(self, observer):
        """Подключить наблюдателя к объекту наблюдения"""
        pass

    def detach(self, observer):
        """Отключить наблюдателя от объекту наблюдения"""
        pass

    def notify(self):
        """Отправить уведомления наблюдателям, подключенным к объекту наблюдения"""
        pass
