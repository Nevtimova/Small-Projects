# progress.py
class ProgressTracker:
    def __init__(self):
        self.logs = []

    def log_workout(self, workout):
        self.logs.append(workout)

    def view_progress(self):
        return "\n".join(workout.view_workout() for workout in self.logs)
