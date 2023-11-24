from brain_games.engine import engine
from brain_games.games.prime import prime
from brain_games.constants import PRIME_GREETING


def main():
    engine(PRIME_GREETING, prime)


if __name__ == '__main__':
    main()
