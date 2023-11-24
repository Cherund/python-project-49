from brain_games.utils import random_number


def greatest_common_divider():
    number_list = [random_number(), random_number()]
    number_list.sort()

    for divisor in range(number_list[0], 0, -1):
        if not number_list[0] % divisor and not number_list[1] % divisor:
            correct_answer = str(divisor)
            break

    print(f'Question: {number_list[0]} {number_list[1]}')

    return correct_answer
