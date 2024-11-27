from brain_games.utils import get_random_number
from brain_games.consts import BRAIN_EVEN_RULES, MIN_NUMBER, MAX_NUMBER_EVEN
from brain_games.game_engine import run_game


def is_even(n):
    return n % 2 == 0


def generate_round():
    number = get_random_number(MIN_NUMBER, MAX_NUMBER_EVEN)
    question = f"{number}"
    correct_answer = "yes" if is_even(number) else "no"
    return question, str(correct_answer)


def even_game():
    run_game(BRAIN_EVEN_RULES, generate_round)
