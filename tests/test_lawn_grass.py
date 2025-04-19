import pytest

from src.lawn_grass import LawnGrass
from src.product import Product


@pytest.fixture
def lawn_grass():
    return LawnGrass("Premium Grass", "Soft", 500, 100, "USA", "2 weeks", "Green")


def test_lawn_grass_init(lawn_grass):
    assert lawn_grass.name == "Premium Grass"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 100
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "2 weeks"
    assert lawn_grass.color == "Green"


def test_lawn_grass_inheritance(lawn_grass):
    assert isinstance(lawn_grass, Product)


def test_lawn_grass_add_valid(lawn_grass):
    other = LawnGrass("Standard Grass", "Hard", 300, 50, "Canada", "3 weeks", "Dark Green")
    total = (lawn_grass.price * lawn_grass.quantity) + (other.price * other.quantity)
    assert lawn_grass + other == total


def test_lawn_grass_add_invalid(lawn_grass):
    from src.smartphone import Smartphone

    other = Smartphone("iPhone", "256GB", 100000, 5, "A15", "14 Pro", "256GB", "White")
    with pytest.raises(TypeError):
        lawn_grass + other
