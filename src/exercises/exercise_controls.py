from datetime import datetime
from matplotlib import pyplot as plt
from src.data_controls import load_data, save_data
from src.exercises.exercise import Exercise


def add_exercise():
    exercises = load_data('data/exercises.json', Exercise)

    while True:
        print("\nEnter the name for the exercise:")
        print("Type 's' to save new exercises or 'q' to quit without saving.")

        exercise_name = input("Exercise name: ").strip()

        if exercise_name.lower() in ['s', 'q']:
            if exercise_name.lower() == 's':
                save_data('data/exercises.json', exercises)
                print("Exercises saved to 'exercises.json'.")
            break

        exercise = next((ex for ex in exercises if ex.name == exercise_name), None)

        if exercise is None:
            exercise = Exercise(exercise_name)
            exercises.append(exercise)

        print(f"Added: {exercise.name}")

def list_exercises(page_size=5):
    exercises = load_data('data/exercises.json', Exercise)

    if not exercises:
        print("No exercises found.")
        return 
    
    total_exercises = len(exercises)
    total_pages = (total_exercises + page_size - 1) // page_size
    current_page = 0

    while True:
        start_index = current_page * page_size
        end_index = min(start_index + page_size, total_exercises)

        print(f'\nExercises (Page {current_page + 1}/{total_pages}):')
        for i in range(start_index, end_index):
            print(f"{i + 1}. {exercises[i].name}")

        print("\nType the number of the exercise to view progress or remove it.")
        command = input("Enter 'n' for next page, 'p' for previous page, 'r' to remove an exercise, 'v' to view progress, or 'q' to quit: ").strip().lower()

        if command == 'n':
            if current_page < total_pages - 1:
                current_page += 1
            else:
                print("You are already on the last page.")
        elif command == 'p':
            if current_page > 0:
                current_page -= 1
            else:
                print("You are already on the first page.")
        elif command == 'r':
            try:
                remove_index = int(input(f"Enter the number of the exercise to remove (1-{total_exercises}): ")) - 1
                if 0 <= remove_index < total_exercises:
                    removed_exercise = exercises.pop(remove_index)
                    total_exercises -= 1
                    save_data('data/exercises.json', exercises)
                    print(f"Removed exercise: {removed_exercise.name}")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        elif command == 'v':
            try:
                view_index = int(input(f"Enter the number of the exercise to view progress (1-{total_exercises}): ")) - 1
                if 0 <= view_index < total_exercises:
                    plot_exercise_progress(exercises[view_index])
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        elif command == 'q':
            break
        else:
            print("Invalid input, please enter 'n', 'p', 'r', 'v', or 'q'.")

def plot_exercise_progress(exercise):
    if not exercise.history:
        print(f"No history available for {exercise.name}.")
        return

    dates = [datetime.strptime(entry['date'], "%Y-%m-%d") for entry in exercise.history]
    scores = [entry['sets'] * entry['reps'] * entry['weight'] for entry in exercise.history]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, scores, marker='o', linestyle='-', color='b', label='Score (sets * reps * weight)')

    plt.title(f"Progress of {exercise.name} Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Score", fontsize=12)
    plt.grid(True)
    plt.legend()

    plt.show()