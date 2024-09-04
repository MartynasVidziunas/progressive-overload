

from src.data_controls import load_data, save_data
import json

from src.exercises.exercise import Exercise
from src.workouts.workout import Workout

def list_workouts(page_size = 5):
    workouts = load_data('data/workouts.json', Workout)

    if not workouts:
        print("\nNo workouts found.")
        return
    
    total_workouts = len(workouts)
    total_pages = (total_workouts + page_size - 1) // page_size
    current_page = 0

    while True:
        total_pages = (total_workouts + page_size - 1) // page_size

        if current_page >= total_pages:
            current_page = max(total_pages - 1, 0)

        start_index = current_page * page_size
        end_index = min(start_index + page_size, total_workouts)

        print(f'\nWorkouts (Page {current_page + 1}/{total_pages}):')
        for i in range(start_index, end_index):
            workout = workouts[i]
            print(f"{i + 1}. {workout.name} - {len(workout.exercises)} exercises")
        
        print("\nType the number of the workout you want to remove, or press enter to continue.")
        command = input("Enter 'n' for next page, 'p' for previous page, 'r' to remove a workout, or 'q' to quit: ").strip().lower()

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
                remove_index = int(input(f"Enter the number of the workout to remove (1-{total_workouts}): ")) - 1
                if 0 <= remove_index < total_workouts:
                    removed_workout = workouts.pop(remove_index)
                    total_workouts -= 1
                    save_data('data/workouts.json', workouts)
                    print(f"Removed workout: {removed_workout.name}")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        elif command == 'q':
            break
        else:
            print("Invalid input, please enter 'n', 'p', 'r', or 'q'.")

def add_workouts():
    workouts = load_data('data/workouts.json', Workout)
    exercises = load_data('data/exercises.json', Exercise)

    workout_name = input("\nWorkout name: ").strip()

    workout = next((wo for wo in workouts if wo.name == workout_name), None)
    if workout is None:
        workout = Workout(workout_name)
        workouts.append(workout)

    print("Type 's' to save the workout, 'q' to quit without saving, or 'a' to add more exercises.")

    while True:
        exercise_name = input("Enter the name of an exercise to assign it to the workout: ").strip()

        if exercise_name.lower() in ['s', 'q']:
            if exercise_name.lower() == 's':
                if len(workout.exercises) >= 3:
                    save_data('data/workouts.json', workouts)
                    print("Workout saved to 'workouts.json'.")
                else:
                    print("You need to add at least 3 exercises before saving.")
            break

        exercise = next((ex for ex in exercises if ex.name.lower() == exercise_name.lower()), None)
        if exercise is None:
            create_exercise = input("Do you want to add this exercise? (y/n): ").strip().lower()
            if create_exercise == 'y':
                exercise = Exercise(exercise_name)
                exercises.append(exercise)
                save_data('data/exercises.json', exercises)
                print(f"Exercise '{exercise_name}' added.")
            else:
                continue
        
        sets = int(input("\nPlease input the number of sets for this exercise: "))
        reps = int(input("Please input the number of reps for this exercise: "))
        weight = float(input("Please input the weight used for this exercise: "))
        

        workout_exercise = Exercise(exercise_name)
        workout_exercise.add_workout(sets, reps, weight)
        workout.add_exercise(workout_exercise)

        print(f"\nAdded exercise '{exercise_name}' with {sets} sets, {reps} reps, and {weight} weight to the workout '{workout_name}'.")

        if len(workout.exercises) < 3:
            print("Workout was not saved yet because it doesn't have at least 3 exercises.")
        else:
            print("Workout has 3 exercises assigned and can be saved now.")

def record_workout_performance():
    workouts = load_data('data/workouts.json', Workout)
    exercises = load_data('data/exercises.json', Exercise)

    if not workouts:
        print("No workouts available.")
        return
    
    print("\nAvailable Workouts:")
    for i, workout in enumerate(workouts):
        print(f"{i + 1}. {workout.name}")

    try:
        workout_index = int(input("Select a workout by number: ")) - 1
        if workout_index < 0 or workout_index >= len(workouts):
            print("Invalid workout number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    selected_workout = workouts[workout_index]
    print(f"\nSelected Workout: {selected_workout.name}")

    for i, exercise in enumerate(selected_workout.exercises):
        print(f"\nExercise {i + 1}: {exercise.name}")

        try:
            sets = int(input("Enter the number of sets: "))
            reps = int(input("Enter the number of reps: "))
            weight = float(input("Enter the weight used: "))
        except ValueError:
            print("Please enter valid numbers for sets, reps, and weight.")
            continue

        existing_exercise = next((ex for ex in exercises if ex.name == exercise.name), None)
        if existing_exercise:
            existing_exercise.add_workout(sets, reps, weight)
            print(f"Recorded {sets} sets, {reps} reps, and {weight} weight for {exercise.name}.")
        else:
            print(f"Error: Exercise {exercise.name} not found in the exercises list.")
    
    save_data('data/exercises.json', exercises)
    print("\nWorkout performance has been recorded.")

def save_data(filename, data):
    with open(filename, 'w') as file:
        data_list = [item.to_dict() for item in data]
        json.dump(data_list, file, indent=4)

