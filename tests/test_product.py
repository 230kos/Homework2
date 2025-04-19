import pytest

from src.exceptions import ZeroQuantityError
from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_create():
    product = Product("Samsung", "Серый цвет", 180000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_upgrade(capsys, product):
    product.price = -1000
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 180000.0
    product.price = 1000
    assert product.price == 1000


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_full_price1, product_full_price2):
    expected_sum = (product_full_price1.price * product_full_price1.quantity) + (
        product_full_price2.price * product_full_price2.quantity
    )
    assert product_full_price1 + product_full_price2 == expected_sum


def test_zero_quantity_product():
    with pytest.raises(ZeroQuantityError):
        Product("Zero", "Test", 100.0, 0)
