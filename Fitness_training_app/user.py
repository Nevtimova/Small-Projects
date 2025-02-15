# user.py
class User:
    def __init__(self, name, age, weight, height, fitness_goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.fitness_goal = fitness_goal

    def update_profile(self, weight=None, fitness_goal=None):
        if weight:
            self.weight = weight
        if fitness_goal:
            self.fitness_goal = fitness_goal

    def view_profile(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg, Height: {self.height}cm, Goal: {self.fitness_goal}"