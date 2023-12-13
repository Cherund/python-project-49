from brain_games.engine import run_game
from brain_games.utils import create_random_number
from brain_games.constants import PRIME_INSTRUCTION


def is_prime(number):
    for divider in range(2, (number // 2) + 1):
        if not number % divider:
            return False
    return True


def get_number_and_prime_answer():
    number = create_random_number()
    prime_answer = 'yes' if is_prime(number) else 'no'

    return number, prime_answer


def run_prime_game():
    run_game(PRIME_INSTRUCTION, get_number_and_prime_answer)
