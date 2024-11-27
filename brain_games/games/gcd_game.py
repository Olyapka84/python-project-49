from brain_games.utils import get_random_number
from math import gcd
from brain_games.consts import BRAIN_GCD_RULES, MIN_NUMBER, MAX_NUMBER_GCD
from brain_games.game_engine import run_game


def generate_round():
    number1, number2 = (get_random_number(MIN_NUMBER, MAX_NUMBER_GCD),
                        get_random_number(MIN_NUMBER, MAX_NUMBER_GCD))
    question = f"{number1} {number2}"
    correct_answer = gcd(number1, number2)
    return question, str(correct_answer)


def gcd_game():
    run_game(BRAIN_GCD_RULES, generate_round)
