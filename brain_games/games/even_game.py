from brain_games.random_for_games import randint_with_range
from brain_games.rules import BRAIN_EVEN_RULES
from brain_games.game_engine import run_game


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def generate_round():
    number = randint_with_range(1, 1000)
    question = f"Question: {number}"
    correct_answer = "yes" if is_even(number) else "no"
    return question, str(correct_answer)


def even_game():
    rules = BRAIN_EVEN_RULES
    run_game(rules, generate_round)
