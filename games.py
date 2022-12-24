# Модуль games
# Демонстрирует создание модуля

import easygui as gui


def ask_yes_no(question, title='Game'):
    """Задает вопрос с ответом (y/n)."""
    return gui.ynbox(question, title)


def ask_number(question, low, high, title='Game'):
    """Просит ввести число из заданного диапазона."""
    return gui.integerbox(question, title, default=int((low+high)/2), lowerbound=low, upperbound=high)


if __name__ == "__main__":
    gui.msgbox("Вы запустили модуль games, "
               "а не импортировали его (import games)."
               "\nТестирование модуля.")
    answer = ask_yes_no("Продолжаем тестирование")
    gui.msgbox("Функция ask_yes_no вернула " + str(answer))
    answer = ask_number("Введите целое число от 1 до 10:", 1, 10)
    gui.msgbox("Функция ask_number вернула " + str(answer))
