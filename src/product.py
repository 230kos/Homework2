from src.base_product import BaseProduct
from src.exceptions import ZeroQuantityError
from typing import Any, Dict, List, Tuple, Type, TypeVar

T = TypeVar('T', bound='Product')

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

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

        super().__init__(name, description, price, quantity)
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls: Type[T], name: str, description: str, price: float, quantity: int) -> T:
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для цены товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены товара"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

