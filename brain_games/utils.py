from random import randint


def generate_random_number(start=2, end=99):
    return randint(start, end)


def strip_to_lower(string):
    return string.strip().lower()
