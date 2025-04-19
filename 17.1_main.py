from src.category import Category
from src.product import Product

if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())

# Дополнительный функционал (проверка задания со звездочкой)
if __name__ == '__main__':
    # Основной код выполнится первым
    pass

# Отдельный блок для тестирования дополнительного функционала
if __name__ == '__main__additional__':
    print("\nТестирование дополнительного функционала:")

    try:
        category = Category("Тест", "Тестовая категория", [])
        zero_product = Product("Нулевой товар", "Тест", 100, 0)
        category.add_product(zero_product)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    try:
        category = Category("Тест", "Тестовая категория", [])
        valid_product = Product("Нормальный товар", "Тест", 100, 10)
        category.add_product(valid_product)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

