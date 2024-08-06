#!/usr/bin/env python3


from brain_games.game_logic import play
from brain_games.games import gcd_game


def main():
    """Функция определяет наибольший общий делитель
    между двумя случайными числами в мини-игре GCD-game.
    """
    play(gcd_game)


if __name__ == '__main__':
    main()
