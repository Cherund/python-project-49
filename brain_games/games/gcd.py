from random import randint
from prompt import string
from brain_games.cli import welcome_user, game_end


def gcd():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    result = 0
    while result < 3:
        number_list = [randint(2, 99), randint(2, 99)]
        print(number_list)
        number_list.sort()

        for divisor in range(number_list[0], 0, -1):
            if not number_list[0] % divisor and not number_list[1] % divisor:
                correct_answer = str(divisor)
                break

        print(f'Question: {number_list[0]} {number_list[1]}')
        player_answer = string('Your answer: ')

        if player_answer.strip() == correct_answer:
            print('Correct!')
            result += 1
        else:
            break

    game_end(player_answer, correct_answer, result, name)
