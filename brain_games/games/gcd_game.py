from brain_games.random_for_games import get_random_number
from math import gcd
from brain_games.rules import BRAIN_GCD_RULES
from brain_games.game_engine import run_game


def generate_round():
    number1 = get_random_number(0, 10)
    number2 = get_random_number(0, 10)
    question = f"Question: {number1} {number2}"
    correct_answer = gcd(number1, number2)
    return question, str(correct_answer)


def gcd_game():
    rules = BRAIN_GCD_RULES
    run_game(rules, generate_round)
