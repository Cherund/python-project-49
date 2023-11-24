from brain_games.utils import random_number


def even():
    number = random_number()
    correct_answer = number % 2
    print(f'Question: {number}')

    if correct_answer:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return correct_answer
