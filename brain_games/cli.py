import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_end(player_answer, correct_answer, result, name):
    if result < 3:
        print(f"'{player_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')
