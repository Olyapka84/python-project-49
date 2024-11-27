from brain_games.random_for_games import get_random_number
from brain_games.rules import BRAIN_PRIME_RULES
from brain_games.game_engine import run_game


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generate_round():
    number = get_random_number(1, 100)
    question = f"{number}"
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def prime_game():
    run_game(BRAIN_PRIME_RULES, generate_round)
