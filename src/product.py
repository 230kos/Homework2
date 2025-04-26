from typing import Any

from src.base_product import BaseProduct
from src.exceptions import ZeroQuantityError


class PrintMixin:
    """Миксин для вывода информации о создании объекта"""

    def __repr__(self) -> str:
        attrs = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({attrs})"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(f"Создан объект {self.__class__.__name__} с параметрами: {self.__repr__()}")
        super().__init__(*args, **kwargs)


class Product(BaseProduct, PrintMixin):
    """Класс для продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация продукта

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара

        Raises:
            ZeroQuantityError: Если количество равно 0
        """
        super().__init__()  # Явный вызов __init__ родительского класса
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int) -> "Product":
        """Создает новый экземпляр продукта"""
        return cls(name, description, price, quantity)

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение продуктов по общей стоимости"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self) -> float:
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену товара"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
