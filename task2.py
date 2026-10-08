import re


def generator_numbers(text):
    # Знаходимо числа з крапкою. Поки що це рядки.
    numbers = re.findall(r"\d+\.\d+", text)

    # Перетворюємо кожен рядок на число й віддаємо по одному.
    for number in numbers:
        yield float(number)


def sum_profit(text, func):
    # Початкова сума.
    total = 0

    # Отримуємо числа через передану функцію та додаємо їх.
    for number in func(text):
        total += number

    # Повертаємо суму після завершення всього циклу.
    return total


# Перевірка роботи.
text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими "
    "надходженнями 27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")