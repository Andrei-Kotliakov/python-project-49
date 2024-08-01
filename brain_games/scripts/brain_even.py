#!/usr/bin/env python3


import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    tries_count = 3
    while tries_count:
        random_num = randint(1, 100)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and random_num % 2 == 0) or (answer == 'no' and random_num % 2 != 0):
            print('Correct!')
            tries_count -= 1
        elif (answer == 'yes' and random_num % 2 != 0):
            print(f'{"yes"} is wrong answer ;(. Correct answer was {"no"}')
            print(f'Let\'s try again, {name}!')
            break
        elif (answer == 'no' and random_num % 2 == 0):
            print(f'{"no"} is wrong answer ;(. Correct answer was {"yes"}.')
            print(f'Let\'s try again, {name}!')
            break
        else:
            if random_num % 2 == 0:
                print(f'"{answer}" is wrong answer ;(. '
                      f'Correct answer was "yes".')
                print(f'Let\'s try again, {name}!')
                break
            else:
                print(f'"{answer}" is wrong answer ;(. '
                      f'Correct answer was "no".')
                print(f'Let\'s try again, {name}!')
                break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
