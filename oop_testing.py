import random
import os

class Question:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.operators = ['+', '-', '*', '/']
        self.num1 = None
        self.num2 = None
        self.operator = None
        self.correct_answer = None
        self.choices = []
        self.correct_index = None

        self._generate_question()
        self._generate_choices()

    def _get_range(self):
        ranges = {
            'easy': (1, 10),
            'medium': (1, 100),
            'hard': (1, 1000),
            'expert': (1, 10000)
        }
        return ranges.get(self.difficulty, (1, 10))

    def _generate_question(self):
        min_val, max_val = self._get_range()
        self.operator = random.choice(self.operators)

        while True:
            self.num1 = random.randint(min_val, max_val)
            self.num2 = random.randint(min_val, max_val)

            if self.operator == '/' and self.num2 != 0 and self.num1 % self.num2 == 0:
                self.correct_answer = self.num1 // self.num2
                break
            elif self.operator == '+':
                self.correct_answer = self.num1 + self.num2
                break
            elif self.operator == '-':
                self.correct_answer = self.num1 - self.num2
                break
            elif self.operator == '*':
                self.correct_answer = self.num1 * self.num2
                break

    def _generate_choices(self):
        self.choices = []
        while len(self.choices) < 3:
            fake = self.correct_answer + random.randint(-10, 10)
            if fake != self.correct_answer and fake not in self.choices:
                self.choices.append(fake)

        self.correct_index = random.randint(0, 3)
        self.choices.insert(self.correct_index, self.correct_answer)

    def display(self, index):
        labels = ['a', 'b', 'c', 'd']
        print(f"\nQuestion {index}: {self.num1} {self.operator} {self.num2}")
        for i, choice in enumerate(self.choices):
            print(f"  {labels[i]}) {choice}")

    def is_correct(self, user_choice):
        labels = ['a', 'b', 'c', 'd']
        return labels.index(user_choice) == self.correct_index

    def get_correct_label(self):
        return ['a', 'b', 'c', 'd'][self.correct_index]


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
            user_input = self._get_user_input()
            self.user_answers.append(f"{i}.{user_input}")
            self.correct_answers.append(f"{i}.{question.get_correct_label()}")

    def _get_user_input(self):
        while True:
            choice = input("Your answer (a/b/c/d): ").lower()
            if choice in self.labels:
                return choice
            print("Invalid input. Please choose a, b, c, or d.")

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

# Run the quiz
if __name__ == "__main__":
    quiz = Quiz()
    quiz.start()
