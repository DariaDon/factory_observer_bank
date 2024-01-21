from abc import ABC, abstractmethod

class Observer(ABC):
    """Абстрактный наблюдатель"""

    @abstractmethod
    def update(self):
        pass


class Client(Observer):
    """Клиент, подавший заявку на кредит"""

    def __init__(self, name: str):
        self.name = name

    # def update(self, state: str):
    #     print(f'Клиент: {self.name}, {state}')
