from brain_games.engine import run_game_engine
from brain_games.utils import generate_random_number
from brain_games.constants import PROGRESSION_LENGTH, PROGRESSION_INSTRUCTION


def create_progression():
    step = generate_random_number(1, 20)
    numbers_list = [str(generate_random_number(1, 50)), ]

    for i in range(PROGRESSION_LENGTH):
        next_number = int(numbers_list[i]) + step
        numbers_list.append(str(next_number))

    removed_index = generate_random_number(0, 9)
    correct_answer = numbers_list[removed_index]
    numbers_list[removed_index] = ".."

    return f'{" ".join(numbers_list)}', correct_answer


def run_progression():
    run_game_engine(PROGRESSION_INSTRUCTION, create_progression)
