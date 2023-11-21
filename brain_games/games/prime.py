from random import randint


def prime():
    number = randint(5, 101)
    correct_answer = 'yes'
    for divider in range(2, number // 2):
        if not number % divider:
            correct_answer = 'no'
            break
    print(f'Question: {number}')
    return correct_answer
