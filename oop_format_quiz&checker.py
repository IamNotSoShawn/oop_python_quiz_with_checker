
# PYTHON QUIZ
import random
import os

print("\nWelcome please choose the difficulty for the math questions you are going to be asked with. \n\n easy is 1 - 10 \n medium is 1 - 100 \n hard is 1 - 1000 \n expert is 1 - 10000 \n ")

def generate_question(difficulty):
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)

    # I added a difficulty adjustment function to cater for different levels of mathematical skill
    if difficulty == 'easy':
        min_val, max_val = 1, 10
    elif difficulty == 'medium':
        min_val, max_val = 1, 100
    elif difficulty == 'hard':
        min_val, max_val = 1, 1000
    else:
        min_val, max_val = 1, 10000

    while True:
        num1 = random.randint(min_val, max_val)
        num2 = random.randint(min_val, max_val)
        if operator == '/' and num2 != 0 and num1 % num2 == 0:
            break
        elif operator != '/':
            break

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    elif operator == '/':
        correct_answer = num1 // num2

    question_text = (num1, operator, num2)
    return question_text, correct_answer

def generate_choices(correct_answer):
    choices = []
    while len(choices) < 3:
        fake = correct_answer + random.randint(-10, 10)
        if fake != correct_answer and fake not in choices:
            choices.append(fake)

    correct_position = random.randint(0, 3)
    choices.insert(correct_position, correct_answer)
    return choices, correct_position

def main():
    labels = ['a', 'b', 'c', 'd']
    user_answers = []
    correct_answers = []

    # Ask user for difficulty
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard/expert): ").lower()
        if difficulty in ['easy', 'medium', 'hard','expert']:
            break
        print("Invalid choice. Please type easy, medium, or hard.")

    with open("answers.txt", "w") as ans_file, open("correct_answers.txt", "w") as corr_file:
        for i in range(1, 11):
            question, correct = generate_question(difficulty)
            choices, correct_index = generate_choices(correct)

            print(f"\nQuestion {i}: {question[0]} {question[1]} {question[2]}")
            for options, choice in enumerate(choices):
                print(f"  {labels[options]}) {choice}")

            while True:
                user_input = input("Your answer (a/b/c/d): ").lower()
                if user_input in labels:
                    break
                print("Invalid input. Please choose a, b, c, or d.")

            user_answers.append(f"{i}.{user_input}")
            correct_answers.append(f"{i}.{labels[correct_index]}")

            ans_file.write(f"{i}.{user_input}\n")
            corr_file.write(f"{i}.{labels[correct_index]}\n")

        print("\nYour answers:")
        for ans in user_answers:
            print(ans)

    print("\nSaving files to:", os.getcwd()) #directory of the current python file
    print("Thank you for using my program !")
if __name__ == "__main__":
    main()

###################################################################################################
# QUIZ CHECKER

def load_answers(filename):
    answers = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(".")
                if len(parts) == 2:
                    q_num, answer = parts
                    answers[int(q_num)] = answer.lower()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    return answers

def check_answers(user_file="answers.txt", correct_file="correct_answers.txt"):
    user_answers = load_answers(user_file)
    correct_answers = load_answers(correct_file)

    if user_answers is None or correct_answers is None:
        return

    print("\n--- Quiz Results ---")
    score = 0
    total = len(correct_answers)

    for q_num in sorted(correct_answers.keys()):
        user_ans = user_answers.get(q_num)
        correct_ans = correct_answers[q_num]
        result = "✅ Correct" if user_ans == correct_ans else f"❌ Wrong (Correct: {correct_ans})"
        print(f"Q{q_num}: You answered '{user_ans}' — {result}")
        if user_ans == correct_ans:
            score += 1

    print(f"\nFinal Score: {score} out of {total}")

if __name__ == "__main__":
    check_answers()
    
