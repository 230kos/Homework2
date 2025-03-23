from typing import Any

from src.category import Category
from src.products import Product


def test_category_init(category: Category) -> None:
    """Тест инициализации объекта Category."""
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products_in_list) == 1


def test_add_product_and_count(category: Category, product: Product) -> None:
    """Тест на добавление продукта в категорию и подсчет продуктов."""
    # Убедимся, что в начале в категории только один продукт
    assert len(category.products_in_list) == 1

    # Добавляем новый продукт
    new_product = product
    category.add_product(new_product)

    # Проверяем, что теперь в категории 2 продукта
    assert len(category.products_in_list) == 2


def test_total_products(category: Category) -> None:
    """Тест на общее количество продуктов в категории."""
    assert len(category.products_in_list) == 1  # Проверяем, что в категории 1 продукт


def test_category_property(category: Category) -> None:
    """Тест на корректность строкового представления продуктов."""
    assert category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_category_setter(category: Any, product: Any) -> None:
    """Тест на добавление продукта через сеттер."""
    assert len(category.products_in_list) == 1
    category.products = product
    assert len(category.products_in_list) == 2
