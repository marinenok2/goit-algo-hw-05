# Декоратор обробляє помилки у функціях команд
def input_error(func):
    def inner(*args, **kwargs):
        try:
            # Запускаємо функцію та повертаємо її результат
            return func(*args, **kwargs)

        except ValueError:
            # Передали неправильну кількість аргументів
            return "Give me name and phone please."

        except KeyError:
            # Такого імені немає у словнику контактів
            return "Contact not found."

        except IndexError:
            # Не передали ім'я для пошуку номера
            return "Enter user name."

    # Повертаємо функцію з обробкою помилок
    return inner


# Розділяємо введений текст на команду та аргументи
def parse_input(user_input):
    parts = user_input.split()

    # Якщо користувач нічого не ввів
    if not parts:
        return "", []

    # Перше слово — команда
    command = parts[0].lower()

    # Решта слів — аргументи команди
    args = parts[1:]

    return command, args


# Додаємо контакт
@input_error
def add_contact(args, contacts):
    # Дістаємо ім'я та телефон зі списку аргументів
    name, phone = args

    # Зберігаємо телефон за ключем — ім'ям
    contacts[name] = phone

    return "Contact added."


# Змінюємо номер наявного контакту
@input_error
def change_contact(args, contacts):
    name, phone = args

    # Якщо контакту немає, викликаємо помилку
    # Її перехопить наш декоратор
    if name not in contacts:
        raise KeyError(name)

    # Замінюємо старий номер новим
    contacts[name] = phone

    return "Contact updated."


# Повертаємо номер за ім'ям
@input_error
def show_phone(args, contacts):
    # Беремо перший аргумент — ім'я
    name = args[0]

    # Шукаємо номер у словнику
    return contacts[name]


# Повертаємо текст з усіма контактами
@input_error
def show_all(args, contacts):
    # Перевіряємо, чи словник порожній
    if not contacts:
        return "No contacts."

    result = ""

    # Перебираємо імена та телефони
    for name, phone in contacts.items():
        # Кожен контакт додаємо з нового рядка
        result += f"{name}: {phone}\n"

    return result


# Основна функція бота
def main():
    # Тут зберігаємо контакти під час роботи програми
    contacts = {}

    print("Welcome to the assistant bot!")

    # Повторюємо введення команд до виходу з програми
    while True:
        user_input = input("Enter a command: ")

        # Отримуємо команду та її аргументи
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(args, contacts))

        else:
            print("Invalid command.")


# Запускаємо бота, якщо запускаємо саме цей файл
if __name__ == "__main__":
    main()