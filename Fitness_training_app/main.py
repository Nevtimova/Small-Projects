# main.py
from Fitness_training_app.exercise import Exercise
from Fitness_training_app.progress import ProgressTracker
from Fitness_training_app.user import User
from Fitness_training_app.workout import Workout


def main():
    user = User("John Doe", 25, 70, 175, "Build muscle")
    exercises = [
        Exercise("Squat", "Lower body strength exercise", "Medium"),
        Exercise("Push-up", "Upper body strength exercise", "Easy")
    ]
    workout = Workout()
    progress = ProgressTracker()

    while True:
        print("\nFitness Training App")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. View Exercises")
        print("4. Create/Modify Workout")
        print("5. Track Progress")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(user.view_profile())
        elif choice == "2":
            weight = input("Enter new weight (or press enter to skip): ")
            goal = input("Enter new fitness goal (or press enter to skip): ")
            user.update_profile(weight=int(weight) if weight else None, fitness_goal=goal if goal else None)
        elif choice == "3":
            for ex in exercises:
                print(ex.view_exercise())
        elif choice == "4":
            print("Available Exercises:")
            for i, ex in enumerate(exercises, 1):
                print(f"{i}. {ex.name}")
            ex_choice = int(input("Choose an exercise by number: ")) - 1
            sets = int(input("Sets: "))
            reps = int(input("Reps: "))
            rest = int(input("Rest time (seconds): "))
            workout.add_exercise(exercises[ex_choice], sets, reps, rest)
            print("Workout updated!")
        elif choice == "5":
            progress.log_workout(workout)
            print("Workout logged. Progress:")
            print(progress.view_progress())
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
