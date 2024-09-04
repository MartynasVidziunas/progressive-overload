import unittest

from src.exercises.exercise import Exercise
from src.workouts.workout import Workout

class TestWorkout(unittest.TestCase):

    def setUp(self):
        self.workout_name = "Leg Day"
        self.workout = Workout(self.workout_name)
        self.exercise1 = Exercise("Squat")
        self.exercise2 = Exercise("Lunge")

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, self.workout_name)
        self.assertEqual(len(self.workout.exercises), 0)
        self.assertIsNotNone(self.workout.id)

    def test_add_exercise(self):
        self.workout.add_exercise(self.exercise1)
        self.workout.add_exercise(self.exercise2)
        
        self.assertEqual(len(self.workout.exercises), 2)
        self.assertIn(self.exercise1, self.workout.exercises)
        self.assertIn(self.exercise2, self.workout.exercises)

    def test_invalid_exercise(self):
        self.workout.add_exercise("Not an Exercise")
        self.assertEqual(len(self.workout.exercises), 0)

    def test_str_representation(self):
        self.workout.add_exercise(self.exercise1)
        workout_str = str(self.workout)
        
        self.assertIn(self.workout_name, workout_str)
        self.assertIn(self.exercise1.name, workout_str)