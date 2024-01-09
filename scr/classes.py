import json


class Category:
    """Класс категорий"""

    count_category = 0
    category_list = list()
    products_list = list()
    count_products = 0

    def __init__(self, name: str, description: str):
        self.name = name  # название категории
        self.description = description  # описание категории
        self.__products = Category.products_list  # товары
        Category.count_category += 1
        Category.category_list.append(self)

    def add_product(self, product):
        """
        Добавление продукта в категорию.
        :param product: Продукт, который нужно добавить
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.count_products += 1
        else:
            raise ValueError("Невозможно добавить объект")

    @property
    def products(self):
        return self.__products

    @property
    def get_products(self):
        self.__products = list()
        for pr in Category.products_list:
            self.__products.append(f"{pr.__str__()}")
        return self.__products

    @classmethod
    def new_category(cls, file_path):
        with open(file_path, encoding="utf-8") as fl:
            category_new = json.load(fl)
        for row in category_new:
            name, description = row["name"], row["description"]
            cls(name, description)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.__len__()} шт."


class Product:
    """Класс продуктов"""

    product_list = list()

    def __init__(self, name: str, description: str, quality: int, price: float):
        self.__name = name  # название продукта
        self.__description = description  # описание продукта
        self.__quality = quality  # количество в наличии
        self.__price = price  # цена
        Category.products_list.append(self)
        Category.count_products = len(Category.products_list)

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def quality(self):
        return self.__quality

    @classmethod
    def new_product(cls, file_path):
        with open(file_path, encoding="utf-8") as fl:
            product_new = json.load(fl)
        for row in product_new:
            products = row["products"]
            for product in products:
                name, description, price, quantity = product["name"], product["description"], product["price"], product["quantity"]
                cls(name, description, price, quantity)

    @staticmethod
    def product_object(name: str, description: str, quality: int, price: float):
        for product in Category.products_list:
            if name == product.name:
                if price > product.price:
                    product.price = price
                product.quality += quality
                return product
        new_prod = Product(name, description, quality, price)
        Category.products_list.append(new_prod)
        return new_prod

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        user_answer = input(f"Вы уверены, что хотите изменить цену? (y/n):")
        if user_answer.lower() == 'y':
            self.__price = new_price
            print("Цена успешно изменена.")
        else:
            print("Изменение цены отменено.")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quality} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
            total = self.price * self.quality
            total_other = other.price * other.quality
            return total + total_other
        else:
            raise TypeError


class NextProduct:
    """Итератор, возвращающий каждый продукт по очереди."""
    def __init__(self, categ):
        if not isinstance(categ, Category):
            raise ValueError('Объект не пренадлежит категории')
        self.categ = categ

    def __iter__(self):
        self.iter = self.categ.get_products
        return self

    def __next__(self):
        if len(self.iter) > 0:
            next_pr = self.iter.pop()
            return next_pr
        else:
            raise StopIteration


class Smartphone(Product):

    def __init__(self, name: str,
                 description: str,
                 quality: int,
                 price: float,
                 performance: str,
                 model: str,
                 memory: int,
                 color: str
                 ):
        super().__init__(name, description, quality, price)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name: str,
                 description: str,
                 quality: int,
                 price: float,
                 country: str,
                 period: str,
                 color: str
                 ):
        super().__init__(name, description, quality, price)
        self.country = country
        self.period = period
        self.color = color
