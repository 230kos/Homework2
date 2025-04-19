import pytest

from src.exceptions import AddProductError, ZeroQuantityError


def test_zero_quantity_error():
    with pytest.raises(ZeroQuantityError) as excinfo:
        raise ZeroQuantityError("Test message")
    assert str(excinfo.value) == "Test message"


def test_add_product_error():
    with pytest.raises(AddProductError) as excinfo:
        raise AddProductError("Test message")
    assert str(excinfo.value) == "Test message"
