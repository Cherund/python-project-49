from random import randint, choice
from brain_games.constants import OPERATIONS
from prompt import string


def generate_number(start=2, end=99):
    return randint(start, end)


def choice_of_operator():
    return choice(OPERATIONS)


def ask_question(question):
    return print(f'Question: {question}')


def request_name_or_answer(name=True):
    if name:
        return string('May I have your name? ')
    else:
        return string('Your answer: ')
