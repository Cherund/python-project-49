from brain_games.engine import run_game_engine
from brain_games.utils import generate_random_number, choice_of_operator
from brain_games.constants import CALCULATOR_INSTRUCTION


def calculate():
    number1, number2 = generate_random_number(), generate_random_number()
    operation = choice_of_operator()
    question = f'{number1} {operation} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer


def run_calculator():
    run_game_engine(CALCULATOR_INSTRUCTION, calculate)
