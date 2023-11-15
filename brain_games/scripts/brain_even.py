from random import randint
from prompt import string
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    result = 0
    while result < 3:
        number = randint(3, 99)
        correct_answer = number % 2
        print(f'Question: {number}')
        player_answer = string('Your answer: ')
        if correct_answer:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

        if player_answer.lower() == correct_answer:
            print('Correct!')
            result += 1
        else:
            break

    if result < 3:
        print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {name}!")
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
