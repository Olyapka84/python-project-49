from random import randint
import prompt
from brain_games.scripts.welcome_user import welcome_user
from brain_games.gcd import gcd


def gcd_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    game_counter = 0
    while game_counter < 3:
        number1 = randint(0, 10)
        number2 = randint(0, 10)
        print(f"Question: {number1} {number2}")
        answer = prompt.string('Your answer: ')
        correct_answer = gcd(number1, number2)
        if int(answer) == correct_answer:
            print("Correct!")
            game_counter += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")
