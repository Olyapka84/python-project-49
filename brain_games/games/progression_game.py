from brain_games.random_for_games import get_random_number
from brain_games.rules import BRAIN_PROGRESSION_RULES, PROGRESSION_LENGTH
from brain_games.game_engine import run_game


def make_sequence():
    first_number = get_random_number(1, 100)
    step = get_random_number(1, 5)
    missed_num_index = get_random_number(0, PROGRESSION_LENGTH - 1)
    sequence = [first_number + i * step for i in range(PROGRESSION_LENGTH)]
    correct_answer = str(sequence[missed_num_index])
    sequence[missed_num_index] = ".."
    question = f"Question: {' '.join(map(str, sequence))}"
    return question, correct_answer


def progression_game():
    run_game(BRAIN_PROGRESSION_RULES, make_sequence)
