import prompt


def welcome_user():
    """Функция выводит строку приветствия пользователю по введенному имени"""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
