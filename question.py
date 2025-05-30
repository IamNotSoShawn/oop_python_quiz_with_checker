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
