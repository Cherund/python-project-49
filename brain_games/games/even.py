from random import randint
from prompt import string
from brain_games.cli import welcome_user, game_end


def even():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    result = 0
    while result < 3:
        number = randint(3, 99)
        correct_answer = number % 2
        print(f'Question: {number}')
        player_answer = string('Your answer: ')
        if correct_answer:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

        if player_answer.lower() == correct_answer:
            print('Correct!')
            result += 1
        else:
            break

    game_end(player_answer, correct_answer, result, name)
