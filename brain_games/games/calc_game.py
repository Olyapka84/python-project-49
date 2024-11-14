from random import randint, choice
import prompt
from brain_games.cli import welcome_user


def calc_game():
    name = welcome_user()
    print("What is the result of the expression?")
    game_counter = 0
    while game_counter < 3:
        number1 = randint(0, 50)
        number2 = randint(0, 50)
        operations = ['+', '-', '*']
        operation = choice(operations)
        print(f"Question: {number1} {operation} {number2}")
        answer = prompt.string('Your answer: ')

        if operation == '+':
            correct_answer = number1 + number2
        elif operation == '-':
            correct_answer = number1 - number2
        elif operation == '*':
            correct_answer = number1 * number2

        try:
            if int(answer) == correct_answer:
                print("Correct!")
                game_counter += 1

            else:
                print(
                    f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
                    f"Let's try again, {name}!")
                break
        except ValueError:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")
