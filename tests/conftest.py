import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


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


@pytest.fixture
def smartphone():
    return Smartphone("iPhone 15", "512GB", 120000, 10, "A16", "15 Pro", "512GB", "Black")

@pytest.fixture
def sample_product():
    return Product("Test Product", "Description", 100.0, 10)


@pytest.fixture
def lawn_grass():
    return LawnGrass("Premium Grass", "Soft", 500, 100, "USA", "2 weeks", "Green")