from brain_games.utils import random_number


def prime():
    number = random_number()
    correct_answer = 'yes'
    for divider in range(2, number // 2):
        if not number % divider:
            correct_answer = 'no'
            break
    print(f'Question: {number}')
    return correct_answer
