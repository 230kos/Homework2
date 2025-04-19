import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category(product):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [product])


@pytest.fixture
def product_full_price1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_full_price2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_iterator(category):
    return ProductIterator(category)


@pytest.fixture
def empty_category():
    return Category("Пустая", "Пустая категория", [])


@pytest.fixture
def sample_category():
    p1 = Product("Product1", "Desc1", 100, 5)
    p2 = Product("Product2", "Desc2", 200, 3)
    return Category("Test", "Test Category", [p1, p2])
