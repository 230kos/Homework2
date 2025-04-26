import json
import os
from typing import Any, List

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """
    Читает JSON файл и возвращает его содержимое в виде словаря.

    Args:
        path: Путь к JSON файлу

    Returns:
        Словарь с данными из JSON файла или пустой словарь в случае ошибки
    """
    try:
        full_path = os.path.abspath(path)
        with open(full_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return {}


def create_objects_from_json(data: Any) -> Any:
    """
    Создает объекты Category и Product из данных JSON.

    Args:
        data: Список словарей с данными категорий и товаров

    Returns:
        Список объектов Category
    """
    categories: List[Category] = []
    for category_data in data:
        products: List[Product] = []
        for product_data in category_data["products"]:
            products.append(Product(**product_data))
        category_data["products"] = products
        categories.append(Category(**category_data))
    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    category_data = create_objects_from_json(raw_data)
    for category in category_data:
        print(category)

"""
другой вариант
if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    category_data = create_objects_from_json(raw_data)
    print([str(category) for category in category_data])
"""
