import prompt


def play(calculator):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    tries_count = 3
    while tries_count:
        question, correct_answer = calculator.information()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct')
            tries_count -= 1
        else:
            print(f'{answer} is wrong answer ;(.')
            print(f'Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
