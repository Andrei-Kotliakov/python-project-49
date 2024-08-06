from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    """Функция определяет является ли случайное число в диапазоне от 2 до 100 простым.

    Ключевые аргументы:
    random_number -- случайное число в диапазоне от 2 до 100
    return -- возврат значение функции
    """
    if random_number == 1:
        return False
    elif random_number == 2:
        return True
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            return False
    return True


def make_rules():
    """Функция определяет корректность указанного ответа."""
    question = randint(2, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
