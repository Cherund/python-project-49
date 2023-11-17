from random import randint, choice
from prompt import string
from brain_games.cli import welcome_user, game_end
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def calc():
    name = welcome_user()
    print("What is the result of the expression?")
    result = 0
    while result < 3:
        number1 = randint(2, 99)
        number2 = randint(2, 99)
        operation = choice(['*', '+', '-'])
        correct_answer = str(ops[operation](number1, number2))

        print(f'Question: {number1} {operation} {number2}')
        player_answer = string('Your answer: ')
        if player_answer.strip() == correct_answer:
            print('Correct!')
            result += 1
        else:
            break

    game_end(player_answer, correct_answer, result, name)
