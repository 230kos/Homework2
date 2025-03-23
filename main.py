from src.category import Category
from src.products import Product

if __name__ == "__main__":
    # Создание объектов Product
    product1: Product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2: Product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3: Product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод информации о продуктах
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Создание объекта Category
    category1: Category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Вывод информации о категории
    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products_in_list))  # Используем products_in_list для получения списка продуктов
    print(category1.category_count)
    print(category1.product_count)

    # Создание еще одного продукта и категории
    product4: Product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2: Category = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    # Вывод информации о второй категории
    print(category2.name)
    print(category2.description)
    print(len(category2.products_in_list))  # Используем products_in_list для получения списка продуктов
    print(category2.products)  # Вывод строкового представления продуктов

    # Вывод общих счетчиков категорий и продуктов
    print(Category.category_count)
    print(Category.product_count)
