import pytest

from scr.classes import Category, Product, NextProduct
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
    Category.products_list = list()
    Product.new_product(PRODUCTS_PATH)
    pr_1 = Category.products_list[0]
    assert pr_1.name == "Samsung Galaxy C23 Ultra"


@pytest.mark.parametrize("obj, expected", [(Category("Елочные игрушки", "На НГ"), ['Сыр, 100.5 руб. Остаток: 2 шт.', 'Gbdj, 100.5 руб. Остаток: 2 шт.', 'qqq, 100.5 руб. Остаток: 2 шт.'])])
def test_products(obj, expected):
    Category.products_list = list()
    prod1 = Product("Сыр", "С дырками", 2, 100.50)
    prod2 = Product("Gbdj", "С дырками", 2, 100.50)
    prod3 = Product("qqq", "С дырками", 2, 100.50)

    assert obj.get_products == expected


def test_new_price():
    prod1 = Product("Сыр", "С дырками", 2, 100.50)
    prod1.price = 200
    assert prod1.price == 200


def test_add_product():
    prod1 = Product("Сыр", "С дырками", 2, 20)
    prod2 = Product("Колбаса", "Вареная", 10, 10)
    assert prod1 + prod2 == 140


def test_next_product():
    Category.products_list = list()
    cat = Category("Елочные игрушки", "На НГ")
    prod1 = Product("Сыр", "С дырками", 2, 100.50)
    prod2 = Product("Gbdj", "С дырками", 2, 100.50)
    prod3 = Product("qqq", "С дырками", 2, 100.50)
    r = NextProduct(cat)
    assert list(r) == ['qqq, 100.5 руб. Остаток: 2 шт.', 'Gbdj, 100.5 руб. Остаток: 2 шт.', 'Сыр, 100.5 руб. Остаток: 2 шт.']
