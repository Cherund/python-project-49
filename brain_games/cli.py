import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def answer_check(player_answer, correct_answer, turns):
    if player_answer == correct_answer:
        print('Correct!')
        return turns - 1
    else:
        return False


def game_end(player_answer, correct_answer, turns, name):
    if isinstance(turns, bool):
        print(f"'{player_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')
