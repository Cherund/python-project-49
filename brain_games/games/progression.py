from brain_games.engine import engine
from brain_games.utils import random_number
from brain_games.constants import PROGRESSION_LENGTH, PROGRESSION_GREETING


def run_progression():
    engine(PROGRESSION_GREETING, progression)


def progression():
    step = random_number(1, 20)
    numbers_list = [str(random_number(1, 50)), ]

    for i in range(PROGRESSION_LENGTH):
        next_number = int(numbers_list[i]) + step
        numbers_list.append(str(next_number))

    removed_index = random_number(0, 9)
    correct_answer = numbers_list[removed_index]
    numbers_list[removed_index] = ".."

    print(f'Question: {" ".join(numbers_list)}')
    return correct_answer
