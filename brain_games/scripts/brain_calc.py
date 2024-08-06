#!/usr/bin/env python3


from brain_games.game_logic import play
from brain_games.games import calc_game


def main():
    """Функция реализует результат арифметического
    выражения в мини-игре Calc-game.
    """
    play(calc_game)


if __name__ == '__main__':
    main()
