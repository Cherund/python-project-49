from brain_games.engine import run_game
from brain_games.utils import create_random_number
from brain_games.constants import PROGRESSION_LENGTH, PROGRESSION_INSTRUCTION


def create_progression(start, step, progression_length):
    return [start + step * i for i in range(progression_length)]


def get_progression_and_hidden_number():
    step, start = create_random_number(1, 20), create_random_number(1, 50)
    numbers_list = create_progression(start, step, PROGRESSION_LENGTH)

    removed_index = create_random_number(0, 9)
    hidden_number = numbers_list[removed_index]
    numbers_list[removed_index] = ".."

    return " ".join(map(str, numbers_list)), str(hidden_number)


def run_progression_game():
    run_game(PROGRESSION_INSTRUCTION, get_progression_and_hidden_number)
