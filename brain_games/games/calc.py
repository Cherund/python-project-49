from random import randint, choice
import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def calc():
    number1 = randint(2, 99)
    number2 = randint(2, 99)
    operation = choice(['*', '+', '-'])
    correct_answer = str(OPS[operation](number1, number2))
    print(f'Question: {number1} {operation} {number2}')
    return correct_answer
