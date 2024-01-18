class CategoryError(Exception):
    """Общий класс исключения для категорий"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка скрипта.'

    def __str__(self):
        return self.message


class NoneProductsError(CategoryError):
    """B категории нет товаров"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Отсутствуют товары.'

    def __str__(self):
        return self.message


