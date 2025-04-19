class ZeroQuantityError(ValueError):
    """Исключение для товаров с нулевым количеством"""

    pass


class AddProductError(Exception):
    """Базовое исключение для ошибок добавления товара"""

    pass
