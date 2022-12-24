# Модуль games
# Демонстрирует создание модуля

def ask_yes_no(question):
    """Задает вопрос с ответом (y/n)."""
    response = None
    while response not in ("y", "n"):
        response = input(question + ' (y/n)? ').lower()
    return response


def ask_number(question, low, high):
    """Просит ввести число из заданного диапазона."""
    response = None
    while response not in range(low, high + 1):
        response = int(input(question))
    return response


if __name__ == "__main__":
    print("Вы запустили модуль games, "
          "а не импортировали его (import games).")
    print("Тестирование модуля.")
    answer = ask_yes_no("Продолжаем тестирование")
    print("Функция ask_yes_no вернула", answer)
    answer = ask_number("Введите целое число от 1 до 10:", 1, 10)
    print("Функция ask_number вернула", answer)
