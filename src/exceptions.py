class ZeroQuantityError(ValueError):
    """Исключение для товаров с нулевым количеством"""

    pass


class AddProductError(Exception):
    """Исключение для ошибок добавления товара"""

    pass
