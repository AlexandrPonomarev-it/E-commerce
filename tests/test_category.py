import pytest


def test_category_init(first_category, second_category):
    assert first_category.name == "Телевизор"
    assert first_category.description == "Красивый телевизор"
    assert len(first_category.product_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_prod_list_property(first_category):
    assert first_category.products == "Sony, 125000.0 руб. Остаток: 5 шт.\nYandex, 133000.0 руб. Остаток: 3 шт.\n"

def test_category_prod_list_add(first_category, product):
    assert len(first_category.product_in_list) == 2
    first_category.add_product(product)
    assert len(first_category.product_in_list) == 3

def test_cat_str(first_category):
    assert str(first_category) == "Телевизор, количество продуктов: 8 шт."

def test_prod_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "PS5"
    assert next(product_iterator).name == "XB"
    assert next(product_iterator).name == "Dendy"

    with pytest.raises(StopIteration):
        next(product_iterator)

def test_category_add_product_setter_error(first_category):
    with pytest.raises(TypeError):
        first_category.add_product(1)

def test_category_add_product_setter(first_category, product_smartphone_1):
    first_category.add_product(product_smartphone_1)
    assert first_category.product_in_list[-1].name == "Samsung Galaxy S23 Ultra"

