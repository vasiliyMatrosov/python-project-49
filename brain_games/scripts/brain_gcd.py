#!/usr/bin/env python3

from brain_games.game_engine import get_logic_of_brain_games
import brain_games.games.logic_brain_gcd


def main():
    get_logic_of_brain_games(brain_games.games.logic_brain_gcd)


if __name__ == '__main__':
    main()
