from brain_games.random_for_games import get_random_number, choose_operation
from brain_games.rules import BRAIN_CALC_RULES, OPERATIONS, MIN_NUMBER, MAX_NUMBER_CALC
from brain_games.game_engine import run_game


def calculate(number1, operation, number2):
    operations = {
        '+': number1 + number2,
        '-': number1 - number2,
        '*': number1 * number2
    }
    return operations[operation]


def generate_round():
    number1, number2 = (get_random_number(MIN_NUMBER, MAX_NUMBER_CALC),
                        get_random_number(MIN_NUMBER, MAX_NUMBER_CALC))
    operation = choose_operation(OPERATIONS)
    question = f"{number1} {operation} {number2}"
    correct_answer = str(calculate(number1, operation, number2))
    return question, correct_answer


def calc_game():
    run_game(BRAIN_CALC_RULES, generate_round)
