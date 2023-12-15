from brain_games.engine import run_game
from brain_games.utils import create_random_number
from brain_games.constants import CALCULATOR_INSTRUCTION, OPERATIONS
import random


def get_expression_and_result():
    number1, number2 = create_random_number(), create_random_number()
    operation = random.choice(OPERATIONS)
    expression = f'{number1} {operation} {number2}'
    result = eval(expression)
    return expression, str(result)


def run_calc_game():
    run_game(CALCULATOR_INSTRUCTION, get_expression_and_result)
