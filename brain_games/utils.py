from random import randint, choice


def get_random_number(start=1, end=99):
    return randint(start, end)


def choose_operation(lst_operation):
    return choice(lst_operation)
