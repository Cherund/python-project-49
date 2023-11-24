from brain_games.engine import engine
from brain_games.games.progression import progression
from brain_games.constants import PROGRESSION_GREETING


def main():
    engine(PROGRESSION_GREETING, progression)


if __name__ == '__main__':
    main()
