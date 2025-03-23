from typing import List

from src.products import Product


class Category:
    """Класс для категорий"""

    # Атрибуты класса для хранения общей информации
    category_count: int = 0  # Общее количество категорий
    product_count: int = 0  # Общее количество товаров

    name: str
    description: str
    __products: List[Product]

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.__products = products if products else []  # Список товаров категории
        Category.category_count += 1  # Увеличиваем количество категорий
        Category.product_count += len(products) if products else 0  # Увеличиваем количество товаров

    def add_product(self, product: Product) -> None:
        """Метод для добавления товара в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
            print(f"Добавлен {product.name} в категорию '{self.name}' (количество: {product.quantity}).")
        else:
            print("Ошибка: В объекте должен быть тип Product.")

    @property
    def products(self) -> str:
        """Метод для получения строкового представления списка товаров."""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @products.setter
    def products(self, product: Product) -> None:
        """Метод для добавления товара в список товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self) -> List[Product]:
        """Метод для получения списка товаров."""
        return self.__products

    def __len__(self) -> int:
        """Метод для возвращения количества продуктов в категории."""
        return sum(product.quantity for product in self.__products)

    def get_product_count(self) -> int:
        """Метод для получения общего количества продуктов в категории."""
        return len(self)

    def __str__(self) -> str:
        return (
            f"Category(name={self.name}, description={self.description},"
            f" number of products={self.get_product_count()})"
        )
