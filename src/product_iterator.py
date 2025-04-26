from typing import Iterator

from src.category import Category
from src.product import Product


class ProductIterator:
    """Итератор для последовательного доступа к товарам категории."""

    def __init__(self, category_obj: Category) -> None:
        self.category1: Category = category_obj
        self.index: int = 0

    def __iter__(self) -> Iterator[Product]:
        self.index = 0
        return self

    def __next__(self) -> Product:
        if self.index < len(self.category1.products_in_list):
            product: Product = self.category1.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    product1: Product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2: Product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3: Product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4: Product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category1: Category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    category2: Category = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    iterator: Iterator[Product] = ProductIterator(category1)

    for product in iterator:
        print(product)
