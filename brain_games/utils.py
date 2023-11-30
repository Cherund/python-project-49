from random import randint, choice
from brain_games.constants import OPERATIONS


def generate_random_number(start=2, end=99):
    return randint(start, end)


def choice_of_operator():
    return choice(OPERATIONS)


def ask_question(question):
    return print(f'Question: {question}')
