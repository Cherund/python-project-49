from random import randint


def even():
    number = randint(3, 99)
    correct_answer = number % 2
    print(f'Question: {number}')

    if correct_answer:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return correct_answer
