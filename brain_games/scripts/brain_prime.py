#!/usr/bin/env python3


from brain_games.game_logic import play
from brain_games.games import prime_game


def main():
    """Функция определяет является ли случайное число
    простым в мини-игре Prime-game.
    """
    play(prime_game)


if __name__ == '__main__':
    main()
