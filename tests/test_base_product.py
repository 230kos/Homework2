from abc import ABC

import pytest

from src.base_product import BaseProduct


def test_base_product_is_abstract():
    """Проверяем, что класс действительно абстрактный"""
    with pytest.raises(TypeError):
        # Попытка создать экземпляр абстрактного класса
        BaseProduct()


def test_base_product_has_required_abstract_methods():
    """Проверяем наличие обязательных абстрактных методов"""
    assert "new_product" in BaseProduct.__abstractmethods__
    assert len(BaseProduct.__abstractmethods__) == 1  # Только new_product должен быть абстрактным


def test_base_product_is_abc():
    """Проверяем, что класс является подклассом ABC"""
    assert issubclass(BaseProduct, ABC)
