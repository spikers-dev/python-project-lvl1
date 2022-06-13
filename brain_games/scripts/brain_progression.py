#!/usr/bin/env python

"""The scripts start the game 'Brain-progression'."""

from brain_games.engine import engine
from brain_games.games import progression


def main():
    """
    Program start.
    Parameters are missing.
    Returns: None
    """
    engine(progression)


if __name__ == '__main__':
    main()
