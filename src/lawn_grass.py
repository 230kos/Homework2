from src.product import Product
from typing import Any, Union


class LawnGrass(Product):
    """Класс для газонной травы, наследуется от Product"""

    country: str
    germination_period: str
    color: str

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ) -> None:
        """
        Инициализация газонной травы

        Args:
            name: Название продукта
            description: Описание
            price: Цена
            quantity: Количество
            country: Страна-производитель
            germination_period: Срок прорастания
            color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> Union[float, Any]:
        """
        Сложение продуктов по общей стоимости

        Args:
            other: Другой продукт того же класса

        Returns:
            Суммарная стоимость товаров

        Raises:
            TypeError: Если объекты разных классов
        """
        if type(other) is not type(self):
            raise TypeError("Можно складывать только объекты одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)
