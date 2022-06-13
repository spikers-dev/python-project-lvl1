#!/usr/bin/env python

"""The scripts start the game 'Brain-prime'"""

from brain_games.engine import engine
from brain_games.games import prime_number


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    engine(prime_number)


if __name__ == '__main__':
    main()
