from src.category import Category
from src.product import Product


def test_product(product):
    assert product.name == "Sony"
    assert product.description == "Жесткая Sony"
    assert product.price == 125000.0
    assert product.quantity == 5


def test_product_new(product_list):
    new_product = Product.new_product({
        "name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 20MP камера", "price": 180000.0,
        "quantity": 5}, product_list)
    new_product.name = "Samsung Galaxy S23 Ultra"
    new_product.description = "256GB, Серый цвет, 20MP камера"
    new_product.price = 180000.0
    new_product.quantity = 5
    new_product.quantity = 10

def test_product_price_property(product):
    assert product.price == 125000.0

def test_product_price_setter(capsys, product):
    product.price = 0
    message = capsys.readouterr()
    assert  message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product.price = -100
    message = capsys.readouterr()
    assert  message.out.strip() == "Цена не должна быть нулевая или отрицательная"



