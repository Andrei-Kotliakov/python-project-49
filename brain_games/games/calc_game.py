from random import randint
from random import choice


THEME = 'What is the result of the expression?'


def information():
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    math_operators = ['+', '-', '*']
    operator = choice(math_operators)
    question = (f'{num_1} {operator} {num_2}')
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    else:
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
