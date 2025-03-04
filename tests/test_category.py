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


