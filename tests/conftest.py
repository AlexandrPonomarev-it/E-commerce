import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProdIterator


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

@pytest.fixture
def product2():
    return Product("Xbox", "Четкий Xbox", 120000.0, 7)


@pytest.fixture
def product_list():
    product_list = [
        Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        ),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]
    return product_list


@pytest.fixture
def product_iterator(second_category):
    return ProdIterator(second_category)