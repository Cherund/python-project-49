from brain_games.engine import run_game_engine
from brain_games.utils import generate_number, ask_question
from brain_games.constants import EVEN_LINE


def find_if_even():
    number = generate_number()
    correct_answer = number % 2

    if correct_answer:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    ask_question(number)
    return correct_answer


def run_even():
    run_game_engine(EVEN_LINE, find_if_even)
