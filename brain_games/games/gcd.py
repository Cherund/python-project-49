from random import randint


def gcd():
    number_list = [randint(2, 99), randint(2, 99)]
    number_list.sort()

    for divisor in range(number_list[0], 0, -1):
        if not number_list[0] % divisor and not number_list[1] % divisor:
            correct_answer = str(divisor)
            break

    print(f'Question: {number_list[0]} {number_list[1]}')

    return correct_answer
