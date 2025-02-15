# workout.py
class Workout:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise, sets, reps, rest_time):
        self.exercises.append({
            'exercise': exercise,
            'sets': sets,
            'reps': reps,
            'rest_time': rest_time
        })

    def view_workout(self):
        return "\n".join(
            f"{ex['exercise'].name}: {ex['sets']} sets of {ex['reps']} reps, Rest: {ex['rest_time']}s"
            for ex in self.exercises
        )