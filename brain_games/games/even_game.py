from random import randint
import prompt
from brain_games.cli import welcome_user


def even_game():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    game_counter = 0
    while game_counter < 3:
        number = randint(1, 1000)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')

        if number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"

        if answer == correct_answer:
            print("Correct!")
            game_counter += 1

        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")
