class Category:
    """Класс категорий"""

    count_category = 0
    count_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name  # название категории
        self.description = description  # описание категории
        self.products = products  # товары
        self.count_category += 1
        self.count_products += len(products)


class Product:
    """Класс продуктов"""

    def __init__(self, name: str, description: str, quality: int, price: float):
        self.name = name  # название продукта
        self.description = description  # описание продукта
        self.quality = quality  # количество в наличии
        self.price = price  # цена
