from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_rules():
    """Функция определяет является ли случайное число
    в диапазоне от 1 до 100 четным/ нечетным.
    """
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
