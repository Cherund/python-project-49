from brain_games.engine import run_game_engine
from brain_games.utils import generate_number, ask_question
from brain_games.constants import PRIME_LINE


def check_for_prime():
    number = generate_number()
    correct_answer = 'yes'
    for divider in range(2, (number // 2) + 1):
        if not number % divider:
            correct_answer = 'no'
            break

    ask_question(number)
    return correct_answer


def run_prime():
    run_game_engine(PRIME_LINE, check_for_prime)
