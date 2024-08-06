from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'
MATH_OPERATORS = ['+', '-', '*']


def make_rules():
    """Функция определяет параметры арифметического выражения,
    формирует выражение и возвращает его результат.
    """
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    operator = choice(MATH_OPERATORS)
    question = (f'{num_1} {operator} {num_2}')
    correct_answer = calculate(num_1, num_2, operator)
    return question, correct_answer


def calculate(num_1, num_2, operator):
    """Функция определяет значение арифметического выражения.

    Ключевые аргументы:
    num_1 -- первое случайное число в пределах от 1 до 10
    num_2 -- второе случайное число в диапазоне от 1 до 10
    operator -- фрифметический оператор
    return -- возврат значения арифметического выражения
    """
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    else:
        correct_answer = num_1 * num_2
    return correct_answer
