from brain_games.utils import get_random_number, choose_operation
from brain_games.consts import BRAIN_CALC_RULES, OPERATIONS
from brain_games.game_engine import run_game


def calculate(number1, operation, number2):
    operations = {
        '+': number1 + number2,
        '-': number1 - number2,
        '*': number1 * number2
    }
    return operations[operation]


def generate_round():
    number1, number2 = get_random_number(), get_random_number()
    operation = choose_operation(OPERATIONS)
    question = f"{number1} {operation} {number2}"
    correct_answer = str(calculate(number1, operation, number2))
    return question, correct_answer


def calc_game():
    run_game(BRAIN_CALC_RULES, generate_round)
