from random import randint, choice
from brain_games.constants import OPS


def random_number(start=2, end=99):
    return randint(start, end)


def choice_of_operator():
    return choice(list(OPS.items()))
