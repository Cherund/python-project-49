from brain_games.engine import engine
from brain_games.games.gcd import greatest_common_divider
from brain_games.constants import GCD_GREETING


def main():
    engine(GCD_GREETING, greatest_common_divider)


if __name__ == '__main__':
    main()
