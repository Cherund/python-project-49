from brain_games.engine import engine
from brain_games.utils import random_number
from brain_games.constants import PRIME_GREETING


def run_prime():
    engine(PRIME_GREETING, prime)


def prime():
    number = random_number()
    correct_answer = 'yes'
    for divider in range(2, (number // 2) + 1):
        if not number % divider:
            correct_answer = 'no'
            break
    print(f'Question: {number}')
    return correct_answer
