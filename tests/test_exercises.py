import unittest
from datetime import datetime
from src.exercises.exercise import Exercise

class TestExercise(unittest.TestCase):

    def setUp(self):
        self.exercise_name = "Bench Press"
        self.exercise = Exercise(self.exercise_name)

    def test_exercise_creation(self):
        self.assertEqual(self.exercise.name, self.exercise_name)
        self.assertEqual(len(self.exercise.history), 0)
        self.assertIsNotNone(self.exercise.id)

    def test_add_workout(self):
        sets = 3
        reps = 10
        weight = 200
        date_time = datetime.now().date().isoformat()
        
        self.exercise.add_workout(sets, reps, weight, date_time)
        
        self.assertEqual(len(self.exercise.history), 1)
        workout = self.exercise.history[0]
        self.assertEqual(workout['sets'], sets)
        self.assertEqual(workout['reps'], reps)
        self.assertEqual(workout['weight'], weight)
        self.assertEqual(workout['date'], date_time)

    def test_str_representation(self):
        sets = 3
        reps = 12
        weight = 150
        self.exercise.add_workout(sets, reps, weight)
        
        exercise_str = str(self.exercise)
        self.assertIn(self.exercise_name, exercise_str)
        self.assertIn("1 entries", exercise_str)