def caching_fibonacci():
    # Створюємо порожній словник для збереження вже обчислених значень
    cache = {}

    # Внутрішня функція для обчислення числа Фібоначчі
    def fibonacci(n):
        # Якщо n менше або дорівнює 0, повертаємо 0
        if n <= 0:
            return 0

        # Якщо n дорівнює 1, повертаємо 1
        if n == 1:
            return 1

        # Якщо значення вже є у кеші, повертаємо його
        if n in cache:
            return cache[n]

        # Якщо значення ще немає у кеші,
        # обчислюємо його за допомогою рекурсії
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        # Повертаємо готове значення з кешу
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci


# Перевірка роботи функції
fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610