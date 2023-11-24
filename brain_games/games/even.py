from brain_games.engine import engine
from brain_games.utils import random_number
from brain_games.constants import EVEN_GREETING


def run_even():
    engine(EVEN_GREETING, even)


def even():
    number = random_number()
    correct_answer = number % 2
    print(f'Question: {number}')

    if correct_answer:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return correct_answer
