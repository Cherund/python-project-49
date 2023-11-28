from brain_games.engine import run_game_engine
from brain_games.utils import generate_number, choice_of_operator, ask_question
from brain_games.constants import CALCULATOR_LINE


def calculate():
    number1, number2 = generate_number(), generate_number()
    operation = choice_of_operator()
    question = f'{number1} {operation} {number2}'
    correct_answer = str(eval(question))

    ask_question(question)
    return correct_answer


def run_calculator():
    run_game_engine(CALCULATOR_LINE, calculate)
