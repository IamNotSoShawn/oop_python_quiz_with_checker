import os
from question import Question
from utils import get_user_input
from grader import Grader

class Quiz:
    def __init__(self):
        self.difficulty = ''
        self.questions = []
        self.user_answers = []
        self.correct_answers = []
        self.labels = ['a', 'b', 'c', 'd']

    def start(self):
        self._welcome()
        self._set_difficulty()
        self._generate_questions()
        self._ask_questions()
        self._save_results()
        self._show_summary()
        self._grade_quiz()

    def _welcome(self):
        print("\nWelcome! Choose the difficulty for the math questions:\n")
        print("  easy    -> numbers between 1 - 10")
        print("  medium  -> numbers between 1 - 100")
        print("  hard    -> numbers between 1 - 1000")
        print("  expert  -> numbers between 1 - 10000\n")

    def _set_difficulty(self):
        while True:
            choice = input("Choose difficulty (easy/medium/hard/expert): ").lower()
            if choice in ['easy', 'medium', 'hard', 'expert']:
                self.difficulty = choice
                break
            print("Invalid choice. Please choose from easy, medium, hard, expert.")

    def _generate_questions(self):
        self.questions = [Question(self.difficulty) for _ in range(10)]

    def _ask_questions(self):
        for i, question in enumerate(self.questions, 1):
            question.display(i)
            user_input = get_user_input(self.labels)
            self.user_answers.append(f"{i}.{user_input}")
            self.correct_answers.append(f"{i}.{question.get_correct_label()}")

    def _save_results(self):
        with open("answers.txt", "w") as ans_file, open("correct_answers.txt", "w") as corr_file:
            for ans in self.user_answers:
                ans_file.write(ans + "\n")
            for correct in self.correct_answers:
                corr_file.write(correct + "\n")

    def _show_summary(self):
        print("\nYour answers:")
        for ans in self.user_answers:
            print(ans)
        print("\nFiles saved to:", os.getcwd())
        print("Thank you for using the quiz program!")

    def _grade_quiz(self):
        grader = Grader()
        grader.grade()
