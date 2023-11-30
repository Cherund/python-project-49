from brain_games.utils import ask_question
from brain_games.constants import GAME_TURNS
import prompt


def run_game_engine(instruction, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{instruction}')

    for _ in range(GAME_TURNS):
        question, correct_answer = get_question_and_answer()
        ask_question(question)
        player_answer = prompt.string('Your answer: ')
        if player_answer.lower().strip() == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
