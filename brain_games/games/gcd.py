from brain_games.engine import run_game_engine
from brain_games.utils import generate_random_number
from brain_games.constants import GCD_INSTRUCTION
from math import gcd


def find_gcd():
    number1, number2 = generate_random_number(), generate_random_number()
    correct_answer = str(gcd(number1, number2))

    return f'{number1} {number2}', correct_answer


def run_greatest_common_divider():
    run_game_engine(GCD_INSTRUCTION, find_gcd)
