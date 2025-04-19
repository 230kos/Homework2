from src.product import Product
from typing import Any, Union


class Smartphone(Product):
    """Класс для смартфонов, наследуется от Product"""

    efficiency: str
    model: str
    memory: str
    color: str

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: str,
            model: str,
            memory: str,
            color: str,
    ) -> None:
        """
        Инициализация смартфона

        :param name: Название смартфона
        :param description: Описание
        :param price: Цена
        :param quantity: Количество
        :param efficiency: Производительность
        :param model: Модель
        :param memory: Объем памяти
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> Union[float, Any]:
        """
        Сложение смартфонов по общей стоимости

        :param other: Другой смартфон того же класса
        :return: Суммарная стоимость
        :raises TypeError: Если объекты разных классов
        """
        if type(other) is not type(self):
            raise TypeError("Можно складывать только объекты одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)

