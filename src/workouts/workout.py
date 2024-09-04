import uuid

from src.exercises.exercise import Exercise

class Workout:

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise):
        if isinstance(exercise, Exercise):
            self.exercises.append(exercise)
        else:
            print("Invalid exercise object provided.")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'exercises': [exercise.to_dict() for exercise in self.exercises]
        }

    @classmethod
    def from_dict(cls, data):
        workout = cls(data['name'])
        workout.id = data['id']
        workout.exercises = [Exercise.from_dict(ex) for ex in data.get('exercises', [])]
        return workout

    def __str__(self):
        exercise_list = ', '.join([exercise.name for exercise in self.exercises])
        return f"Workout: {self.name}, Exercises: {exercise_list}"
      