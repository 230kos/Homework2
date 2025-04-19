from abc import ABC, abstractmethod
from typing import Any, Union


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество товара
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта"""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> Union[float, Any]:
        """
        Сложение продуктов

        Args:
            other: Другой продукт для сложения

        Returns:
            Результат сложения (обычно общая стоимость)

        Raises:
            TypeError: Если сложение невозможно
        """
        pass
