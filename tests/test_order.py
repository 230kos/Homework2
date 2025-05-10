import pytest

from src.exceptions import ZeroQuantityError
from src.order import Order


def test_order_init(sample_product):
    order = Order(sample_product, 3)
    assert order.product == sample_product
    assert order.quantity == 3
    assert order.total_price == 300.0


def test_order_str(sample_product):
    order = Order(sample_product, 2)
    assert str(order) == "Заказ Test Product: Test Product, Количество: 2, Итого: 200.0 руб."


def test_order_zero_quantity(sample_product):
    with pytest.raises(ZeroQuantityError):  # Изменили ValueError на ZeroQuantityError
        Order(sample_product, 0)

    with pytest.raises(ZeroQuantityError):
        Order(sample_product, -5)  # Добавили тест на отрицательное количество
