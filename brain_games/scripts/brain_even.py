#!/usr/bin/env python3


from brain_games.game_logic import play
from brain_games.games import even_game


def main():
    """Функция реализует проверку случайного числа
    на четность в мини-игре Even-game.
    """
    play(even_game)


if __name__ == '__main__':
    main()
