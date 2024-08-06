#!/usr/bin/env python3


from brain_games.game_logic import play
from brain_games.games import progression_game


def main():
    """Функция определяет пропущенное число из случайного списка
    арифметической прогрессии в мини-игре Progression-game.
    """
    play(progression_game)


if __name__ == '__main__':
    main()
