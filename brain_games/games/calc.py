from brain_games.engine import run_game
from brain_games.utils import create_random_number
from brain_games.constants import CALCULATOR_INSTRUCTION, OPERATIONS
import random


def get_equation_and_result():
    number1, number2 = create_random_number(), create_random_number()
    operation = random.choice(OPERATIONS)
    equation = f'{number1} {operation} {number2}'
    correct_answer = str(eval(equation))
    return equation, correct_answer


def run_calc_game():
    run_game(CALCULATOR_INSTRUCTION, get_equation_and_result)
