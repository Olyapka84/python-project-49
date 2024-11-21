from brain_games.random_for_games import randint_with_range
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
    number = randint_with_range(1, 100)
    question = f"Question: {number}"
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def prime_game():
    rules = BRAIN_PRIME_RULES
    run_game(rules, generate_round)
