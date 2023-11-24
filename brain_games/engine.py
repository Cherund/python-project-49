from prompt import string
from brain_games.constants import TURNS


def engine(greeting_message, game_function):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{greeting_message}')

    for _ in range(TURNS):
        correct_answer = game_function()
        player_answer = string('Your answer: ')
        if player_answer.lower().strip() == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return

        print(f'Congratulations, {name}!')
