import pytest

from src.product import Product


def test_product_init(product: Product) -> None:
    """Тест инициализации объекта Product."""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_create() -> None:
    """Тест создания объекта Product."""
    product = Product("Samsung", "Серый цвет", 180000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_upgrade(capsys: pytest.CaptureFixture, product: Product) -> None:
    """Тест изменения цены продукта."""
    # Попытка установить отрицательную цену
    product.price = -1000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 180000.0  # Цена не изменилась

    # Установка корректной цены
    product.price = 1000
    assert product.price == 1000  # Цена успешно изменена
