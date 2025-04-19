import pytest

from src.abstract_entity import AbstractEntity


def test_abstract_entity_is_abstract():
    with pytest.raises(TypeError):
        AbstractEntity("Test", "Description")


def test_abstract_entity_methods():
    assert "__init__" in AbstractEntity.__abstractmethods__
    assert "__str__" in AbstractEntity.__abstractmethods__


class TestConcreteEntity(AbstractEntity):
    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        return f"{self.name}: {self.description}"


def test_concrete_entity_implementation():
    entity = TestConcreteEntity("Test", "Description")
    assert entity.name == "Test"
    assert entity.description == "Description"
    assert str(entity) == "Test: Description"
