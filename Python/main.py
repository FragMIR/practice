# ---------------------------------------------------- Import Block ----------------------------------------------------
# Importing required libreries
import random
import time
import os

# -------------------------------------------------- Veriebles Block ---------------------------------------------------
userResponse = ""

introductionText = "Данная программа демонстрирует решение задач по программированию." \
                   "\nДля тестирования работы программ воспользуйтесь меню:"

programMainMenu = ["1. Запуск заданий", "2. Листинг заданий", "3. Выход из программы"]

programRunMenu = ["1. Запустить выполнение задания №1 'ASCII символы'",
                  "2. Запустить выполнение задания №2 'Наибольшая цифра'",
                  "3. Запустить выполнение задания №3 'Большие по модулю'",
                  "4. Запустить выполнение задания №4 'Разряды числа'",
                  "5. Запустить выполнение задания №5 'Сумма чисел'",
                  "6. Выйти в главное меню"]

programListingMenu = ["1. Вывести код задания №1 'ASCII символы'",
                      "2. Вывести код задания №2 'Наибольшая цифра'",
                      "3. Вывести код задания №3 'Большие по модулю'",
                      "4. Вывести код задания №4 'Разряды числа'",
                      "5. Вывести код задания №5 'Сумма чисел'",
                      "6. Выйти в главное меню"]

taskMenu = ["1. Запустить повторно",
            "2. Вывести код решения",
            "3. Выйти в главное меню",
            "4. Закрыть программу"]


# --------------------------------------------- Function Defenition Block ----------------------------------------------

# Task #1
def task1():
    pass


# End of Task


# Task #2
def task2():
    pass


# End of Task


# Task #3
def task3():
    pass


# End of Task


# Task #4
def task4():
    pass


# End of Task


# Task #5
def task5():
    pass


# End of Task


# Response handling function
def response_handler(message, flag):
    if flag == 1:
        match int(message):
            case [1]:
                print("Задание №1 'ASCII символы':\n")
                task1()
            case [2]:
                print("Задание №2 'Наибольшая цифра':\n")
                task2()
            case [3]:
                print("Задание №3 'Большие по модулю':\n")
                task3()
            case [4]:
                print("Задание №4 'Разряды числа':\n")
                task4()
            case [5]:
                print("Задание №5 'Сумма чисел':\n")
                task5()
            case _:
                return 0
    elif flag == 2:
        try:
            with open("main.py", "r", encoding="utf-8") as s_file:
                sourceCode = s_file.read()
                sourceCode = sourceCode.split("# End of Task")
                s_file.close()
        except:
            print("Внимание! Не удалось прочесть файл исходного кода.")
            return 0

        match int(message):
            case [1]:
                print(sourceCode[0])
                return 1
            case [2]:
                print(sourceCode[1])
                return 1
            case [3]:
                print(sourceCode[2])
                return 1
            case [4]:
                print(sourceCode[3])
                return 1
            case [5]:
                print(sourceCode[4])
                return 1
            case _:
                return 0

def main():
    # Printing the program description
    print(introductionText + "\n")
    runtime_handler = 0

    # Main loop
    while runtime_handler >= 0:

        # User choose to run tasks (1)
        if runtime_handler == 1:
            for line in programRunMenu:
                print(line)
            userResponse = input(">: ")
            if response_handler(userResponse, runtime_handler) == 0: runtime_handler = 0
            else:
                pass

        # User choose to view task's listing (2)
        elif runtime_handler == 2:
            for line in programListingMenu:
                print(line)
            userResponse = input(">: ")
            if response_handler(userResponse, runtime_handler) == 0: runtime_handler = 0
            else:
                pass

        # User choose main manu (0)
        else:
            for line in programMainMenu:
                print(line)
            userResponse = input(">: ")
            if userResponse == "1": runtime_handler = 1
            elif userResponse == "2": runtime_handler = 2
            elif userResponse == "3": runtime_handler = -1
            else:
                print("Данного пункта нет в меню!\nВведите 1, 2 или 3")
                runtime_handler = 0

    # Exiting the program
    print("Спасибо что ознакомились с программой! ☺")
    time.sleep(3)

# Running main
if __name__ == "__main__":
    main()
