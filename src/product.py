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

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Метод для создания нового продукта из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

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

    def __str__(self) -> str:
        """Метод для строкового представления продукта."""
        return (
            f"Product(name={self.name}, description={self.description}, "
            f"price={self.price}, quantity={self.quantity})"
        )
