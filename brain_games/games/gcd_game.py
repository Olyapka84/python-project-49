from math import gcd

from brain_games.consts import BRAIN_GCD_RULES
from brain_games.game_engine import run_game
from brain_games.utils import get_random_number


def generate_round():
    number1, number2 = get_random_number(), get_random_number()
    question = f"{number1} {number2}"
    correct_answer = gcd(number1, number2)
    return question, str(correct_answer)


def gcd_game():
    run_game(BRAIN_GCD_RULES, generate_round)
