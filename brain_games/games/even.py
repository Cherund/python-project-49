from brain_games.engine import run_game
from brain_games.utils import create_random_number
from brain_games.constants import EVEN_INSTRUCTION


def is_even(number):
    return number % 2 == 0


def get_number_and_even_answer():
    number = create_random_number()
    correct_answer = 'yes' if is_even(number) else 'no'

    return number, correct_answer


def run_even_game():
    run_game(EVEN_INSTRUCTION, get_number_and_even_answer)
