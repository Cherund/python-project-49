from random import randint
from prompt import string
from brain_games.cli import welcome_user, game_end


def progression():
    name = welcome_user()
    print("What number is missing in the progression?")
    result = 0
    while result < 3:
        step = randint(1, 20)
        numbers_list = [str(randint(1, 50)), ]

        for i in range(9):
            next_number = int(numbers_list[i]) + step
            numbers_list.append(str(next_number))

        removed_index = randint(0, 9)
        correct_answer = numbers_list[removed_index]
        numbers_list[removed_index] = ".."

        print(f'Question: {" ".join(numbers_list)}')
        player_answer = string('Your answer: ')

        if player_answer.strip() == correct_answer:
            print('Correct!')
            result += 1
        else:
            break

    game_end(player_answer, correct_answer, result, name)
