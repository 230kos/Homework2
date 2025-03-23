import json
import os
from typing import Any, Dict, List

from src.category import Category
from src.products import Product


def read_json(path: str) -> Any:
    """Чтение JSON-файла и возвращение данных в виде списка словарей."""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def create_objects_from_json(data: List[Dict[str, Any]]) -> List[Category]:
    """Создание объектов Category и Product из данных JSON."""
    categories: List[Category] = []
    for category_data in data:
        products: List[Product] = []
        for product_data in category_data["products"]:
            products.append(Product(**product_data))
        category_data["products"] = products
        categories.append(Category(**category_data))
    return categories


if __name__ == "__main__":
    raw_data: List[Dict[str, Any]] = read_json("../data/products.json")
    category_data: List[Category] = create_objects_from_json(raw_data)
    print(category_data)
