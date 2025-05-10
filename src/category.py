from typing import List, Optional

from src.abstract_entity import AbstractEntity
from src.exceptions import AddProductError, ZeroQuantityError
from src.product import Product


class Category(AbstractEntity):
    """Класс для категорий"""

    category_count: int = 0
    product_count: int = 0
    __products: List[Product]  # Явная аннотация для приватного атрибута.

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        super().__init__(name, description)
        self.__products = []
        for product in products if products else []:
            try:
                self.add_product(product)
            except AddProductError as e:
                print(f"Ошибка при добавлении товара: {e}")

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию"""
        try:
            if not isinstance(product, Product):
                raise AddProductError("Можно добавлять только объекты класса Product или его наследников")

            if product.quantity == 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")

            self.__products.append(product)
            Category.product_count += 1
            print(f"Товар {product.name} успешно добавлен")

        except Exception as e:
            raise AddProductError(str(e))
        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self) -> float:
        """Рассчитывает среднюю цену товаров в категории"""
        try:
            total = sum(product.price for product in self.__products)
            return float(total / len(self.__products))  # Явное приведение к float
        except ZeroDivisionError:
            return 0.0  # Возвращаем float вместо int

    @property
    def products(self) -> str:
        """Возвращает строковое представление списка товаров"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_in_list(self) -> List[Product]:
        """Возвращает список товаров"""
        return self.__products

    def __len__(self) -> int:
        """Возвращает общее количество товаров в категории"""
        return sum(product.quantity for product in self.__products)
