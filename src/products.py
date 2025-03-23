class Product:
    """Класс для продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.__price = price  # Цена товара
        self.quantity = quantity  # Количество в наличии

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int) -> "Product":
        """Метод для создания нового продукта."""
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для цены товара."""
        return self.__price

    @price.setter
    def price(self, new_price: str) -> None:
        """Сеттер для цены товара."""
        try:
            new_price_float = float(new_price)
            if new_price_float <= 0:
                print("Цена не должна быть нулевая или отрицательная")
                return
            self.__price = new_price_float
        except ValueError:
            print("Ошибка: Некорректное значение цены.")

    def __str__(self) -> str:
        """Метод для строкового представления продукта."""
        return (
            f"Product(name={self.name}, description={self.description}, "
            f"price={self.price}, quantity={self.quantity})"
        )
