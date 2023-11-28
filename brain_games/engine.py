from brain_games.utils import request_name_or_answer
from brain_games.constants import GAME_TURNS


def run_game_engine(game_line, get_answer):
    print('Welcome to the Brain Games!')
    name = request_name_or_answer()
    print(f'Hello, {name}!\n'
          f'{game_line}')

    for _ in range(GAME_TURNS):
        correct_answer = get_answer()
        player_answer = request_name_or_answer(name=False)
        if player_answer.lower().strip() == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
