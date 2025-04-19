import pytest
from src.base_product import BaseProduct


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Test", "Description", 100, 5)


def test_base_product_methods():
    assert "__init__" in BaseProduct.__abstractmethods__
    assert "__str__" in BaseProduct.__abstractmethods__
    assert "__add__" in BaseProduct.__abstractmethods__


class TestConcreteProduct(BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name} - {self.price}"

    def __add__(self, other):
        return self.price + other.price


def test_concrete_product_implementation():
    product1 = TestConcreteProduct("Test1", "Desc1", 100, 5)
    product2 = TestConcreteProduct("Test2", "Desc2", 200, 3)

    assert product1.name == "Test1"
    assert product1.price == 100
    assert str(product1) == "Test1 - 100"
    assert product1 + product2 == 300
