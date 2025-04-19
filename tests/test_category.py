import pytest

from src.category import Category
from src.exceptions import AddProductError, ZeroQuantityError
from src.product import Product


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products_in_list) == 1


def test_add_product_and_count(category, product):
    assert len(category.products_in_list) == 1
    new_product = Product("New Product", "Desc", 1000.0, 2)
    category.add_product(new_product)
    assert len(category.products_in_list) == 2


def test_total_products(category):
    assert len(category.products_in_list) == 1


def test_category_property(category):
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in category.products


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 5 шт."


def test_middle_price(category):
    assert category.middle_price() == 180000.0


def test_empty_category_middle_price():
    empty_category = Category("Пустая", "Нет товаров", [])
    assert empty_category.middle_price() == 0


def test_add_zero_quantity_product(category):
    with pytest.raises(ZeroQuantityError):
        Product("Zero", "Test", 100.0, 0)


def test_add_invalid_product(category):
    with pytest.raises(AddProductError):
        category.add_product("not a product")
