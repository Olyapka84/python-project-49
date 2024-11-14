from random import randint, choice
import prompt
from brain_games.cli import welcome_user


def progression_game():
    name = welcome_user()
    print("What number is missing in the progression?")
    game_counter = 0
    while game_counter < 3:
        start_sequence = randint(1, 100)
        step_sequence = randint(1, 5)
        sequence = [start_sequence + i * step_sequence for i in range(10)]
        hidden_number = choice(sequence)
        hidden_number_index = sequence.index(hidden_number)
        sequence[hidden_number_index] = ".."
        print(f"Question: {' '.join(str(item) for item in sequence)}")
        answer = prompt.string('Your answer: ')
        correct_answer = hidden_number
        try:
            if int(answer) == correct_answer:
                print("Correct!")
                game_counter += 1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
                      f"Let's try again, {name}!")
                break
        except ValueError:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
