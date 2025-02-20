import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    return Category(
        name="Телевизор",
        description="Красивый телевизор",
        products=[
            Product("Sony", "Жесткая Sony", 125000.0, 5),
            Product("Yandex", "Мягкий Yandex", 133000.0, 3),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Игровые приставки",
        description="Красивый телевизор",
        products=[
            Product("PS5", "Мечта любого", 55000.0, 5),
            Product("XB", "Тоже ничего", 52000.0, 3),
            Product("Dendy", "Ностальгия", 2500.0, 13),
        ],
    )


@pytest.fixture
def product():
    return Product("Sony", "Жесткая Sony", 125000.0, 5)
