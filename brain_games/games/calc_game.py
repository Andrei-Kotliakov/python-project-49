from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'


def make_rules():
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    math_operators = ['+', '-', '*']
    operator = choice(math_operators)
    question = (f'{num_1} {operator} {num_2}')
    correct_answer = str(calculate()


def calculate(num_1, num_2, operator):
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    else:
        correct_answer = num_1 * num_2
    return correct_answer
