from brain_games.utils import random_number, choice_of_operator


def calculator():
    number1, number2 = random_number(), random_number()
    operation, operation_function = choice_of_operator()
    correct_answer = str(operation_function(number1, number2))
    print(f'Question: {number1} {operation} {number2}')
    return correct_answer
