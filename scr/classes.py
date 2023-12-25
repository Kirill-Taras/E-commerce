import json


class Category:
    """Класс категорий"""

    count_category = 0
    category_list = list()
    products_list = list()
    count_products = 0

    def __init__(self, name: str, description: str):
        self.name = name  # название категории
        self.description = description  # описание категории# товары
        self.__products = Category.products_list
        Category.count_category += 1
        Category.category_list.append(self)

    @classmethod
    def new_category(cls, file_path):
        with open(file_path, encoding="utf-8") as fl:
            category_new = json.load(fl)
        for row in category_new:
            name, description = row["name"], row["description"]
            cls(name, description)


class Product:
    """Класс продуктов"""

    product_list = list()

    def __init__(self, name: str, description: str, quality: int, price: float):
        self.name = name  # название продукта
        self.description = description  # описание продукта
        self.quality = quality  # количество в наличии
        self.price = price  # цена
        Category.products_list.append(self)
        Category.count_products = len(Category.products_list)

    @classmethod
    def new_product(cls, file_path):
        with open(file_path, encoding="utf-8") as fl:
            product_new = json.load(fl)
        for row in product_new:
            products = row["products"]
            for product in products:
                name, description, price, quantity = product["name"], product["description"], product["price"], product["quantity"]
                cls(name, description, price, quantity)
