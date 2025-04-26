from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """ "Абстрактный метод для создания нового продукта"""
        pass
