from brain_games.engine import run_game
from brain_games.utils import create_random_number
from brain_games.constants import GCD_INSTRUCTION
import math


def get_numbers_and_gcd():
    number1, number2 = create_random_number(), create_random_number()
    gcd = str(math.gcd(number1, number2))

    return f'{number1} {number2}', gcd


def run_gcd_game():
    run_game(GCD_INSTRUCTION, get_numbers_and_gcd)
