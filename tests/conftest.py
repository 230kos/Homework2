from typing import Any

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product() -> Any:
    """Фикстура для создания объекта Product."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category(product: Any) -> Any:
    """Фикстура для создания объекта Category с одним продуктом."""
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [product])
