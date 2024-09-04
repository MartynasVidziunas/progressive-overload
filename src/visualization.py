import os

from src.exercises.exercise_controls import add_exercise, list_exercises
from src.mail.mailing import mail_workout
from src.workouts.workout_controls import add_workouts, record_workout_performance, list_workouts


def show_main_menu():

    while True:
        print("\nSelect one of these modes:")
        print("1. Exercises")
        print("2. Workouts")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        match choice:
            case '1':
                show_exercise_menu()
            case '2':
                show_workout_menu()
            case '3':
                os._exit(0)
            case _:
                print("Invalid choice. Please try again.")


def show_exercise_menu():

    while True:
        print('\n1. List exercises')
        print('2. Add exercises')
        print('3. Back to main menu')

        choice = input("Enter choice (1/2/3): ")

        match choice:
            case '1':
                list_exercises()
            case '2':
                add_exercise()
            case '3':
                show_main_menu()
            case _:
                print("Invalid choice. Please try again.")

def show_workout_menu():

    while True:
        print('\n1. List workouts')
        print('2. Add workout')
        print('3. Record performance')
        print('4. E-mail a workout')
        print('5. Back to main menu')

        choice = input("Enter choice (1/2/3/4/5): ")

        match choice:
            case '1':
                list_workouts()
            case '2':
                add_workouts()
            case '3':
                record_workout_performance()
            case '4':
                mail_workout()
            case '5':
                show_main_menu()
            case _:
                print("Invalid choice. Please try again.")


