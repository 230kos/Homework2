from typing import Any

from src.products import Product


def test_product_init(product: Product) -> None:
    """Тест инициализации объекта Product."""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_creat() -> None:
    """Тест создания объекта Product."""
    product: Product = Product("Samsung", "Серый цвет", 180000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_upgread(capsys: Any, product: Any) -> None:
    """Тест изменения цены продукта."""
    # Попытка установить отрицательную цену
    product.price = "-1000"
    messege = capsys.readouterr()
    assert messege.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 180000.0  # Цена не изменилась

    # Установка корректной цены
    product.price = 1000
    assert product.price == 1000  # Цена успешно изменена
