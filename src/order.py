from src.abstract_entity import AbstractEntity
from src.exceptions import ZeroQuantityError
from src.product import Product


class Order(AbstractEntity):
    """Класс для обработки заказов"""

    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ZeroQuantityError("Количество товара в заказе должно быть положительным")

        name = f"Заказ {product.name}"
        description = f"Заказ товара {product.name} в количестве {quantity}"
        super().__init__(name, description)
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        return f"{self.name}: {self.product.name}, " f"Количество: {self.quantity}, " f"Итого: {self.total_price} руб."
