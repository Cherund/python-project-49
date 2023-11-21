from brain_games.cli import welcome_user, game_end, answer_check
from brain_games.games.calc import calc
from brain_games.games.even import even
from brain_games.games.gcd import gcd
from brain_games.games.prime import prime
from brain_games.games.progression import progression
from prompt import string

GAMES_LINES = {
    'calc': "What is the result of the expression?",
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'gcd': "Find the greatest common divisor of given numbers.",
    'prime': 'Answer "yes" if given number is prime. Otherwise answer "no".',
    'progression': "What number is missing in the progression?",
}

GAMES_FUNCTIONS = {
    'calc': calc,
    'even': even,
    'gcd': gcd,
    'prime': prime,
    'progression': progression,
}


def engine(game_name):
    name = welcome_user()
    print(GAMES_LINES[game_name])

    turns = 3
    while turns > 0:
        correct_answer = GAMES_FUNCTIONS[game_name]()
        player_answer = string('Your answer: ')
        turns = answer_check(player_answer, correct_answer, turns)

    game_end(player_answer, correct_answer, turns, name)
