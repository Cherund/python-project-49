from brain_games.engine import run_game_engine
from brain_games.utils import generate_number, ask_question
from brain_games.constants import GCD_LINE
from math import gcd


def find_gcd():
    number1, number2 = generate_number(), generate_number()
    correct_answer = str(gcd(number1, number2))

    ask_question(f'{number1} {number2}')
    return correct_answer


def run_greatest_common_divider():
    run_game_engine(GCD_LINE, find_gcd)
