from brain_games.engine import engine
from brain_games.games.calc import calculator
from brain_games.constants import CALCULATOR_GREETING


def main():
    engine(CALCULATOR_GREETING, calculator)


if __name__ == '__main__':
    main()
