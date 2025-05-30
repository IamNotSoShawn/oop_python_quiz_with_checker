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