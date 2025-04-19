import pytest

from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def smartphone():
    return Smartphone("iPhone 15", "512GB", 120000, 10, "A16", "15 Pro", "512GB", "Black")


def test_smartphone_init(smartphone):
    assert smartphone.name == "iPhone 15"
    assert smartphone.price == 120000
    assert smartphone.quantity == 10
    assert smartphone.efficiency == "A16"
    assert smartphone.model == "15 Pro"
    assert smartphone.memory == "512GB"
    assert smartphone.color == "Black"


def test_smartphone_inheritance(smartphone):
    assert isinstance(smartphone, Product)


def test_smartphone_add_valid(smartphone):
    other = Smartphone("iPhone 14", "256GB", 90000, 5, "A15", "14 Pro", "256GB", "White")
    total = (smartphone.price * smartphone.quantity) + (other.price * other.quantity)
    assert smartphone + other == total


def test_smartphone_add_invalid(smartphone):
    from src.lawn_grass import LawnGrass

    other = LawnGrass("Grass", "Green", 500, 100, "USA", "2 weeks", "Green")
    with pytest.raises(TypeError):
        smartphone + other
