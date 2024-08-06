from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def make_rules():
    """Функция определяет пропущенное чсило в прогрессии случайных чисел."""
    start = randint(1, 24)
    step = randint(1, 7)
    stop = start + step * 10
    stealth_element = randint(0, 9)
    progression = [i for i in range(start, stop, step)]
    progression[stealth_element] = '..'
    question = (' '.join(map(str, progression)))
    correct_answer = start + step * stealth_element
    return question, correct_answer
