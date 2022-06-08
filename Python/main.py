# ---------------------------------------------------- Import Block ----------------------------------------------------
# Importing required libreries
import random
import time

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


# --------------------------------------------- Function Defenition Block ----------------------------------------------

# Task #1
def task1():
    # Printing task Description
    print("Проверка кода символа ASCII - буква или нет.")

    respose = input("Введите код символа ASCII в десятичном формате: ") # Waiting for user input

    # Checking user response to be a letter code in ASCII table
    if int(respose) in range(65,90) or int(respose) in range(97,122): # It is a letter
        print("Это символ латинской буквы.")
        time.sleep(2)
    else: # It isn't letter
        print("Символ не является латинской буквой.")

        # Beautifier
        print("\n")
        time.sleep(2)

# End of Task #1


# Task #2
def task2():
    # Printing task Description
    print("Поиск наибольшей цифры в числе.")

    respose = input("Введите натуральное число: ")  # Waiting for user input

    # Checking user response to be an integer
    try:
        int(respose)  # It is integer
        if int(respose) >= 0:
            print()
            max = 0
            for ch in respose:  # Checking every symbol one at a time
                if max < int(ch): max = int(ch)
            print("Наибольшей является цифра: ",max)
        else:
            print("Это не натуральное число.")
        time.sleep(2)
    except ValueError:  # It isn't integer
        print("Это не целое число.")

    # Beautifier
    print("\n")
    time.sleep(2)


# End of Task #2


# Task #3
def task3():

    # Printing task Description
    print("Поиск количества чисел по модулю больше максимального.")

    num_count = 0
    num_array = []
    for i in range(20):                             # Doing 20 iterations
        num_array.append(random.randint(-15,14))    # Filling the array with random numbers
    max_number = max(num_array)                     # Finding the maximum number (max<i?max=i etc.)

    for i in num_array:                         # Going through the array
        if abs(i) > max_number: num_count+=1    # Counting abses which greater then max_number


    print("Массив случайных чисел: ",num_array)
    print("Максимальное число: ",max_number)
    print("Чисел по модулю больше максимального: ",num_count)

    # Beautifier
    print("\n")
    time.sleep(2)

# End of Task #3


# Task #4
def task4():

    # Printing task Description
    print("Определение количества разрядов в числе.")

    response = input("Введите целое число: ")   # Waiting for user input

    # Checking if user typed a number
    try:
        response = abs(int(response))
        digit_count = 0
        while response > 0:                 # While there is a digit
            response = int(response/10)     # Divide by 10, convert to integer
            digit_count+=1                  # Counting digits
        print("Разрядность числа: ",digit_count)
    except ValueError:                      # User input is not a digit
        print("Невозможно преобразовать в целое число!")

    # Beautifier
    print("\n")
    time.sleep(2)

# End of Task #4


# Task #5
def task5():

    # Printing task Description
    print("Подсчёт суммы введённых чисел.")

    response = input("Вводите числа для подсчёта (начать подсчёт - Enter):\n>:")  # Waiting for user input
    numbers_summ = 0
    while response != "":   # Stops if user just push Enter without input
        try:
            numbers_summ += float(response)
            response = input(">: ")
        except ValueError:
            response = 0
            print("Можно вводить только числа!")

    print("Сумма введённых чисел: ",numbers_summ)

    # Beautifier
    print("\n")
    time.sleep(2)


# End of Task #5


# Response handling function
def response_handler(message, flag):
    if flag == 1:

        # Defining which task to start
        match int(message):
            case 1:
                print("Задание №1:")
                task1()
            case 2:
                print("Задание №2:")
                task2()
            case 3:
                print("Задание №3:")
                task3()
            case 4:
                print("Задание №4:")
                task4()
            case 5:
                print("Задание №5:")
                task5()
            case _:
                return 0
    elif flag == 2:

        # Trying to open the source file
        try:
            with open("main.py", "r", encoding="utf-8") as s_file:
                sourceCode = s_file.read()                      # Reading the source code to sourceCode
                s_file.close()                                  # Closing the file, won't read anything else
        except: # Faild to open the source file
            print("Внимание! Не удалось прочесть файл исходного кода.")
            return 0                                            # Quiting the function


        # Defining which task to print
        match int(message):
            case 1:
                print(sourceCode[sourceCode.index("# Task #1"):sourceCode.index("# End of Task #1")])
                return 1
            case 2:
                print(sourceCode[sourceCode.index("# Task #2"):sourceCode.index("# End of Task #2")])
                return 1
            case 3:
                print(sourceCode[sourceCode.index("# Task #3"):sourceCode.index("# End of Task #3")])
                return 1
            case 4:
                print(sourceCode[sourceCode.index("# Task #4"):sourceCode.index("# End of Task #4")])
                return 1
            case 5:
                print(sourceCode[sourceCode.index("# Task #5"):sourceCode.index("# End of Task #5")])
                return 1
            case _:
                return 0


# --------------------------------------------------- Main Function ---------------------------------------------------
def main():
    # Printing the program description
    print(introductionText + "\n")
    runtime_handler = 0

    # Main loop
    while runtime_handler >= 0:

        # User chose to run tasks (1)
        if runtime_handler == 1:
            for line in programRunMenu:
                print(line)
            print("\n")
            userResponse = input(">: ")
            if response_handler(userResponse, runtime_handler) == 0: runtime_handler = 0

        # User chose to view task's listing (2)
        elif runtime_handler == 2:
            for line in programListingMenu:
                print(line)
            print("\n")
            userResponse = input(">: ")
            if response_handler(userResponse, runtime_handler) == 0: runtime_handler = 0

        # User chose main manu (0)
        else:
            for line in programMainMenu:                        # Printing maine menu
                print(line)
            print("\n")
            userResponse = input(">: ")                         # waiting for user input
            if userResponse == "1": runtime_handler = 1
            elif userResponse == "2": runtime_handler = 2
            elif userResponse == "3": runtime_handler = -1
            else:                                               # Users input is not in the list
                print("Данного пункта нет в меню!\nВведите 1, 2 или 3")
                runtime_handler = 0

    # Exiting the program
    print("Спасибо что ознакомились с программой! ☺")
    time.sleep(3)

# Running main
if __name__ == "__main__":
    main()
