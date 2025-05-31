class Grader:
    def __init__(self, user_file="answers.txt", correct_file="correct_answers.txt"):
        self.user_file = user_file
        self.correct_file = correct_file
        self.user_answers = {}
        self.correct_answers = {}

    def load_answers(self, filename):
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

    def grade(self):
        self.user_answers = self.load_answers(self.user_file)
        self.correct_answers = self.load_answers(self.correct_file)

        if self.user_answers is None or self.correct_answers is None:
            return

        print("\n--- Quiz Results ---")
        score = 0
        total = len(self.correct_answers)

        for q_num in sorted(self.correct_answers.keys()):
            user_ans = self.user_answers.get(q_num)
            correct_ans = self.correct_answers[q_num]
            result = "✅ Correct" if user_ans == correct_ans else f"❌ Wrong (Correct: {correct_ans})"
            print(f"Q{q_num}: You answered '{user_ans}' — {result}")
            if user_ans == correct_ans:
                score += 1

        print(f"\nFinal Score: {score} out of {total}")
