from brain_games.random_for_games import randint_with_range, choose_operation
from brain_games.rules import BRAIN_CALC_RULES
from brain_games.game_engine import run_game


def calculate(number1, operation, number2):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2



def generate_round():
    number1 = randint_with_range(0, 50)
    number2 = randint_with_range(0, 50)
    operation = choose_operation(['+', '-', '*'])
    question = f"Question: {number1} {operation} {number2}"
    correct_answer = calculate(number1, operation, number2)
    return question, str(correct_answer)


def calc_game():
    rules = BRAIN_CALC_RULES
    run_game(rules, generate_round)
