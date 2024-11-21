from brain_games.random_for_games import randint_with_range, choice
from brain_games.rules import BRAIN_PROGRESSION_RULES, PROGRESSION_LENGTH
from brain_games.game_engine import run_game


def make_sequence():
    start_sequence = randint_with_range(1, 100)
    step_sequence = randint_with_range(1, 5)
    hidden_num_index = randint_with_range(0, PROGRESSION_LENGTH - 1)
    sequence = [start_sequence + i * step_sequence for i in range(PROGRESSION_LENGTH)]
    correct_answer = str(sequence[hidden_num_index])
    sequence[hidden_num_index] = ".."
    question = f"Question: {' '.join(str(item) for item in sequence)}"
    return question, correct_answer


def progression_game():
    rules = BRAIN_PROGRESSION_RULES
    run_game(rules, make_sequence)
