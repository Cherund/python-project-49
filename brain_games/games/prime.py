from random import randint
from prompt import string
from brain_games.cli import welcome_user, game_end


def prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime, otherwise answer "no".')
    result = 0
    while result < 3:
        number = randint(5, 101)
        correct_answer = 'yes'
        for divider in range(2, number // 2):
            if not number % divider:
                correct_answer = 'no'
                break
        print(f'Question: {number}')
        player_answer = string('Your answer: ')

        if player_answer.lower() == correct_answer:
            print('Correct!')
            result += 1
        else:
            break

    game_end(player_answer, correct_answer, result, name)
