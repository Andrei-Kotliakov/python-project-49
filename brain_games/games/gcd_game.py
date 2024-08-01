from random import randint
from random import choice
import math


THEME = 'Find the greatest common divisor of given numbers.'


def information():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = (f'{num_1} {num_2}')
    correct_answer = math.gcd(num_1, num_2)
    return question, str(correct_answer)
