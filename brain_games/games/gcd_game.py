from brain_games.random_for_games import randint_with_range
from math import gcd
from brain_games.rules import BRAIN_GCD_RULES
from brain_games.game_engine import run_game


def generate_round():
    number1 = randint_with_range(0, 10)
    number2 = randint_with_range(0, 10)
    question = f"Question: {number1} {number2}"
    correct_answer = gcd(number1, number2)
    return question, str(correct_answer)

def gcd_game():
    rules = BRAIN_GCD_RULES
    run_game(rules, generate_round)
