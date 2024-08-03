from random import randint


THEME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


random_number = randint(2, 100)


def is_prime(random_number):
    if random_number == 2:
        return True
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            return False
    return True


def information():
    question = randint(2, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer