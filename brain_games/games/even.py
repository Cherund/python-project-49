from brain_games.engine import run_game_engine
from brain_games.utils import generate_random_number
from brain_games.constants import EVEN_INSTRUCTION


def check_if_not_even(number):
    return number % 2


def find_if_even():
    number = generate_random_number()
    correct_answer = 'no' if check_if_not_even(number) else 'yes'

    return number, correct_answer


def run_even():
    run_game_engine(EVEN_INSTRUCTION, find_if_even)
