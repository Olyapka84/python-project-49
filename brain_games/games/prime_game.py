from random import randint
import prompt
from brain_games.cli import welcome_user
from brain_games.prime import is_prime


def prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_counter = 0
    while game_counter < 3:
        number = randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        if is_prime(number):
            correct_answer = "yes"
        else:
            correct_answer = "no"
        if answer == correct_answer:
            print("Correct!")
            game_counter += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
