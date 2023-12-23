import pytest

from scr.classes import Category, Product
from scr.config import PRODUCTS_PATH


def test_init_category():
    Category.count_category = 0
    category_1 = Category("Елочные игрушки", "На НГ")
    category_2 = Category("Фрукты", "Еда")
    assert category_1.name == "Елочные игрушки"
    assert category_1.description == "На НГ"
    assert category_2.name == "Фрукты"
    assert category_2.description == "Еда"
    assert Category.count_category == 2


@pytest.fixture()
def test_product():
    return Product("Сыр", "С дырками", 2, 100.50)


def test_init_product(test_product):
    assert test_product.name == "Сыр"
    assert test_product.description == "С дырками"
    assert test_product.quality == 2
    assert test_product.price == 100.50
    assert Category.count_products == 1


def test_new_category():
    Category.category_list = list()
    Category.new_category(PRODUCTS_PATH)
    assert Category.category_list[0].name == "Смартфоны"
    assert Category.category_list[1].name == "Телевизоры"


def test_new_product():
    Category.products = list()
    Product.new_product(PRODUCTS_PATH)
    pr_1 = Category.products[0]
    assert pr_1.name == "Samsung Galaxy C23 Ultra"
