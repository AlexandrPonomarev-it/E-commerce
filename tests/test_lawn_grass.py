import pytest


def test_lawn_grass_product_init(product_lawn_grass_1):
    assert product_lawn_grass_1.name == "Газонная трава"
    assert product_lawn_grass_1.description == "Элитная трава для газона"
    assert product_lawn_grass_1.price == 500.0
    assert product_lawn_grass_1.quantity == 20
    assert product_lawn_grass_1.country == "Россия"
    assert product_lawn_grass_1.germination_period == "7 дней"
    assert product_lawn_grass_1.color == "Зеленый"


def test_lawn_grass_product_add(product_lawn_grass_1, product_lawn_grass_2):
    assert product_lawn_grass_1.price * product_lawn_grass_1.quantity + product_lawn_grass_2.price * product_lawn_grass_2.quantity == 16750.0


def test_lawn_grass_product_add_error(product_lawn_grass_1):
    with pytest.raises(TypeError):
        assert product_lawn_grass_1 + 1