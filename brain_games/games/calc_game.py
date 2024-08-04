from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'
MATH_OPERATORS = ['+', '-', '*']


def make_rules():
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    operator = choice(MATH_OPERATORS)
    question = (f'{num_1} {operator} {num_2}')
    correct_answer = calculate(num_1, num_2, operator)
    return question, correct_answer


def calculate(num_1, num_2, operator):
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    else:
        correct_answer = num_1 * num_2
    return correct_answer
