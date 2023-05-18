# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


def task6():
    GREGORYANSKY_CALENDAR = 1582
    CHECK_NORMAL = 4
    CHECK_HUNDRED = 100
    CHECK_4HUNDRED = 400
    year = int(input("Enter year: "))
    result = ''
    if year < GREGORYANSKY_CALENDAR:
        result = "year before the introduction of the Gregorian calendar"
    elif year % CHECK_NORMAL == 0 and (year % CHECK_HUNDRED != 0 or year % CHECK_4HUNDRED == 0):
        result = "The year is a leap"
    else:
        result = "The year is ordinary"

    print(result)

# task6()

# ----------------------------------------------------------------------------------------------------------

# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


def task7():
    FROM = 1
    TO = 999
    result = ""

    while True:
        input_number = input(f"Enter number from {FROM} to {TO}: ")
        if FROM <= int(input_number) <= TO:
            match len(input_number):
                case 1:
                    result = int(input_number) ** 2
                case 2:
                    result = int(input_number[0]) * int(input_number[1])
                case 3:
                    result = input_number[::-1]
            break

    print(result)

# task7()

# ----------------------------------------------------------------------------------------------------------

# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********


def task8():
    rows = int(input("How many rows do the tree have?"))

    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars + spaces)


# task8()

# ----------------------------------------------------------------------------------------------------------

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


def task9():
    import math

    MIN_NUM = 2
    MAX_NUM = 9
    MIN_FACTOR = 2
    MAX_FACTOR = 10
    COUNT_HORIZONTAL_BLOCKS = 2    # количество горизонтальных блоков

    count_columns = math.ceil((MAX_NUM - MIN_NUM + 1) / COUNT_HORIZONTAL_BLOCKS)
    current_min_number = MIN_NUM     # минимальное число в текущем блоке

    for i in range(1, COUNT_HORIZONTAL_BLOCKS + 1):
        current_max_number = current_min_number + \
            count_columns  # максимальное число в текущем блоке
        if current_max_number > MAX_NUM + 1:
            current_max_number -= 1
        for j in range(MIN_FACTOR, MAX_FACTOR + 1):
            result_row = ""
            for k in range(current_min_number, current_max_number):
                result_row += f"{k} X "
                if j >= 10:
                    result_row += f"{j}= "
                else:
                    result_row += f"{j} = "
                if k * j >= 10:
                    result_row += f"{k * j}"
                else:
                    result_row += f" {k * j}"
                result_row += "     "
            print(result_row)
        print(end="\n")
        current_min_number = current_max_number


# task9()
# ----------------------------------------------------------------------------------------------------------


# ДОМАШНИЕ ЗАДАЧИ
# ----------------------------------------------------------------------------------------------------------

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

def home_task1():
    SIDE_A = 5
    SIDE_B = 5
    SIDE_C = 15
    
    if (SIDE_A + SIDE_B <= SIDE_C) or \
       (SIDE_A + SIDE_C <= SIDE_B) or \
       (SIDE_B + SIDE_C <= SIDE_A):
        print("A triangle with such sides doesn't exist")
    else:
        print("Such a triangle exists")
        if SIDE_A == SIDE_B == SIDE_C:
            print("And this triangle is equilateral")
        elif (SIDE_A == SIDE_B) or \
             (SIDE_A == SIDE_C) or \
             (SIDE_C == SIDE_B):
            print("And this triangle is isosceles")
        else:
            print("And this triangle is versatile")


# home_task1()

# ----------------------------------------------------------------------------------------------------------

# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def home_task2():
    MIN_VALUE = 0 
    MAX_VALUE = 100000
    
    input_number = int(input("Enter your number: "))
    is_a_simple = True
    if MIN_VALUE > input_number or MAX_VALUE < input_number:
        print("Incorrect number")
    else:
        if input_number == 1 or input_number == 0:
            is_a_simple = False
        elif input_number > 2:
            for i in range(2, int(input_number / 2) + 1, 1):
                if input_number % i == 0:
                    is_a_simple = False
        
        print("Your number is a simple" if is_a_simple \
            else "Your number isn't simple")


# home_task2()


# ----------------------------------------------------------------------------------------------------------

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
#  Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:

def home_task3():
    from random import randint
    
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    COUNT_ATTEMPTS = 10
    
    hidden_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    for i in range(1, COUNT_ATTEMPTS + 1):
        user_number = int(input(f"Attempt {i}. Enter your number: "))
        if (user_number < hidden_number):
            print("Upper")
        elif (user_number > hidden_number):
            print("Lower")
        else:
            print("You win!")
            return
    print("The number of attempts is over")
    
# home_task3()



