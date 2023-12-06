from brain_games.engine import run_game
from brain_games.utils import generate_random_number
from brain_games.constants import CALCULATOR_INSTRUCTION, OPERATIONS
import random


def evaluate_equation():
    number1, number2 = generate_random_number(), generate_random_number()
    operation = random.choice(OPERATIONS)
    equation = f'{number1} {operation} {number2}'
    correct_answer = str(eval(equation))
    return equation, correct_answer


def run_calc_game():
    run_game(CALCULATOR_INSTRUCTION, evaluate_equation)
