"""Functions of the game 'Brain-even'."""

from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task_and_solution():
    """
    Get an integer(task) and correct answer/
    Parameters are missing.
    Returns:
        tuple: (int, str)
    """
    task = randint(0, 100)
    correct_answer = 'yes' if task % 2 == 0 else 'no'

    return task, correct_answer