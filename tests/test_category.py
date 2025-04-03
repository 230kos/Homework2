import pytest


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products_in_list) == 1


def test_add_product_and_count(category, product):
    """Тест на добавление продукта в категорию и подсчет продуктов."""
    # Убедимся, что в начале в категории только один продукт
    assert len(category.products_in_list) == 1  # Добавляем новый продукт
    new_product = product
    category.add_product(new_product)  # Добавляем новый продукт # Проверяем, что теперь в категории 2 продукта
    assert len(category.products_in_list) == 2


def test_total_products(category):
    """Тест на общее количество продуктов в категории."""
    assert len(category.products_in_list) == 1  # Проверяем, что в категории 1 продукт


def test_category_property(category):
    assert category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_category_setter(category, product):
    assert len(category.products_in_list) == 1
    category.products = product
    assert len(category.products_in_list) == 2


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 1 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"

    with pytest.raises(StopIteration):
        next(product_iterator)