from random import randint
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_rules():
    """Функция определяет наибольший общий делитель
    двух случайных чисул в диапазоне от 1 до 100.
    """
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = (f'{num_1} {num_2}')
    correct_answer = math.gcd(num_1, num_2)
    return question, correct_answer
