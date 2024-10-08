import prompt


def play(game):
    """

    Функция содержит основную логику серии игр Brain-games,
    включая особенности, такие как:
    приветствие игрока, вывод задания, вывод результата.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    tries_count = 3
    while tries_count:
        question, correct_answer = game.make_rules()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct')
            tries_count -= 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
