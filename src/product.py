class Product:
    """Класс для продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.__price = price  # Цена товара (приватная)
        self.quantity = quantity  # Количество в наличии

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return self.price + other.price

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int) -> "Product":
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для цены товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены товара."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
