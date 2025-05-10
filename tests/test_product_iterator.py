import pytest

from src.product_iterator import ProductIterator


def test_iterator_init(sample_category):
    iterator = ProductIterator(sample_category)
    assert iterator.index == 0
    assert iterator.category1 == sample_category  # Проверяем, что category1 установлен правильно


def test_iterator_next(sample_category):
    iterator = ProductIterator(sample_category)
    products = list(iterator)
    assert len(products) == 2
    assert products[0].name == "Product1"
    assert products[1].name == "Product2"


def test_iterator_stop(sample_category):
    iterator = ProductIterator(sample_category)
    list(iterator)  # Получаем все элементы
    with pytest.raises(StopIteration):
        next(iterator)  # Должно вызвать StopIteration

