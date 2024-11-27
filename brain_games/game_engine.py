from brain_games.cli import welcome_user
import prompt


def run_game(rules, generate_round):
    name = welcome_user()
    print(rules)

    for games in range(3):
        question, correct_answer = generate_round()
        print(f"Question: {question}")

        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {correct_answer}.\n"
                f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
