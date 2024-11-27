from brain_games.random_for_games import get_random_number
from brain_games.rules import (BRAIN_PROGRESSION_RULES, PROGRESSION_LENGTH,
                               MIN_NUMBER, MAX_STEP_PROGRESSION, MAX_NUMBER_PRIME_PROGR)
from brain_games.game_engine import run_game


def make_sequence():
    first_number = get_random_number(MIN_NUMBER, MAX_NUMBER_PRIME_PROGR)
    step = get_random_number(MIN_NUMBER, MAX_STEP_PROGRESSION)
    missed_num_index = get_random_number(MIN_NUMBER, PROGRESSION_LENGTH - 1)
    sequence = [first_number + i * step for i in range(PROGRESSION_LENGTH)]
    correct_answer = str(sequence[missed_num_index])
    sequence[missed_num_index] = ".."
    question = f"{' '.join(map(str, sequence))}"
    return question, correct_answer


def progression_game():
    run_game(BRAIN_PROGRESSION_RULES, make_sequence)
