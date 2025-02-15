# exercise.py
class Exercise:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def view_exercise(self):
        return f"{self.name}: {self.description} (Difficulty: {self.difficulty})"