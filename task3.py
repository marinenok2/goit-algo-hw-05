import sys  # Потрібен, щоб отримати аргументи командного рядка


def parse_log_line(line):
    # Розділяємо один рядок логу на частини за пробілами
    parts = line.split()

    # Створюємо словник з даними одного запису
    log = {
        "date": parts[0],              # Дата
        "time": parts[1],              # Час
        "level": parts[2],             # Рівень: INFO, ERROR тощо
        "message": " ".join(parts[3:])  # Увесь текст повідомлення
    }

    return log


def load_logs(file_path):
    # Тут зберігатимемо всі записи з файлу
    logs = []

    # Відкриваємо файл для читання
    with open(file_path, "r", encoding="utf-8") as file:
        # Читаємо файл рядок за рядком
        for line in file:
            # Пропускаємо порожні рядки
            if line.strip():
                # Перетворюємо рядок на словник
                log = parse_log_line(line)

                # Додаємо словник до списку
                logs.append(log)

    return logs


def count_logs_by_level(logs):
    # У словнику зберігатимемо кількість записів кожного рівня
    counts = {}

    for log in logs:
        # Беремо рівень поточного запису
        level = log["level"]

        if level in counts:
            # Якщо рівень уже є, збільшуємо його кількість
            counts[level] += 1
        else:
            # Якщо бачимо рівень уперше, записуємо 1
            counts[level] = 1

    return counts


def display_log_counts(counts):
    # Виводимо заголовок таблиці
    print("Рівень логування | Кількість")

    # .items() дає назву рівня та його кількість
    for level, count in counts.items():
        print(level, "|", count)


def filter_logs_by_level(logs, level):
    # Тут зберігатимемо записи потрібного рівня
    filtered_logs = []

    for log in logs:
        # upper() дозволяє ввести, наприклад, error замість ERROR
        if log["level"] == level.upper():
            filtered_logs.append(log)

    return filtered_logs


def main():
    # sys.argv[0] — назва скрипта
    # sys.argv[1] — шлях до файлу логів
    # Якщо шлях не передали, показуємо підказку
    if len(sys.argv) < 2:
        print("Вкажіть шлях до файлу логів.")
        return

    file_path = sys.argv[1]

    # Пробуємо прочитати файл
    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        # Цей блок виконається, якщо файлу немає
        print("Файл не знайдено:", file_path)
        return

    # Рахуємо записи кожного рівня та показуємо результат
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # sys.argv[2] — необов'язковий рівень, наприклад error
    if len(sys.argv) > 2:
        level = sys.argv[2]

        # Отримуємо лише записи потрібного рівня
        filtered_logs = filter_logs_by_level(logs, level)

        print("Записи рівня", level.upper())

        # Виводимо кожен знайдений запис
        for log in filtered_logs:
            print(
                log["date"],
                log["time"],
                log["level"],
                log["message"]
            )


# Запускаємо main(), коли запускаємо саме цей файл
if __name__ == "__main__":
    main()