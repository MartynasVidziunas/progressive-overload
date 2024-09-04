import uuid
from datetime import datetime

class Exercise:

    def __init__(self, name, ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.history = []

    def add_workout(self, sets, reps, weight, date_time=None):
        if date_time is None:
            date_time = datetime.now().date().isoformat()

        workout = {
            'sets': sets,
            'reps': reps,
            'weight': weight,
            'date': date_time
        }
        self.history.append(workout)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'history': self.history
        }

    @classmethod
    def from_dict(cls, data):
        exercise = cls(data['name'])
        exercise.id = data['id']
        exercise.history = data.get('history', [])
        return exercise
    
    def __str__(self):
        return f"Exercise: {self.name}, History: {len(self.history)} entries"
      