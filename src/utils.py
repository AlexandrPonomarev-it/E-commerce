import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Функция принимает файл json и возвращает список операций"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list) -> list:
    """Функция принимает список операций и выводит через классы полученные данные"""
    categories = []
    for category in data:
        products = []
        for prod in category["products"]:
            products.append(Product(**prod))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/data.json")
    users_data = create_objects_from_json(raw_data)

    print(users_data)
