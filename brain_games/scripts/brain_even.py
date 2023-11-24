from brain_games.engine import engine
from brain_games.games.even import even
from brain_games.constants import EVEN_GREETING


def main():
    engine(EVEN_GREETING, even)


if __name__ == '__main__':
    main()
