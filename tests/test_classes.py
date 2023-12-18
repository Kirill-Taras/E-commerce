import pytest

from scr.classes import Category, Product


def test_init_category():
    category_1 = Category("Елочные игрушки", "На НГ", ["Шар", "Звезда", "Пряня"])
    category_2 = Category("Фрукты", "Еда", ["Банан", "Киви", "Груша", "Манго"])
    assert category_1.name == "Елочные игрушки"
    assert category_1.description == "На НГ"
    assert category_1.products == ["Шар", "Звезда", "Пряня"]
    assert category_2.name == "Фрукты"
    assert category_2.description == "Еда"
    assert category_2.products == ["Банан", "Киви", "Груша", "Манго"]
    assert Category.count_products == 7
    assert Category.count_category == 2


@pytest.fixture()
def test_product():
    return Product("Сыр", "С дырками", 2, 100.50)


def test_init_product(test_product):
    assert test_product.name == "Сыр"
    assert test_product.description == "С дырками"
    assert test_product.quality == 2
    assert test_product.price == 100.50
