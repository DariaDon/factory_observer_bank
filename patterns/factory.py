from typing import Hashable, Callable
from models import Credit, Observable

class Factory(object):
    """Фабрика создает объекты заявка на кредит"""

    @staticmethod
    def get(class_name: Hashable) -> Observable:

        if not isinstance(class_name, Hashable):
            raise ValueError()

        classes: dict[Hashable, Callable[..., Observable]] = {
            "Credit": Credit
        }

        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_()

        raise ValueError
