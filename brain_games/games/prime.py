from brain_games.engine import run_game_engine
from brain_games.utils import generate_random_number
from brain_games.constants import PRIME_INSTRUCTION


def check_for_prime():
    number = generate_random_number()
    correct_answer = 'yes'
    for divider in range(2, (number // 2) + 1):
        if not number % divider:
            correct_answer = 'no'
            break

    return number, correct_answer


def run_prime():
    run_game_engine(PRIME_INSTRUCTION, check_for_prime)
