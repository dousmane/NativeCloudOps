from . import db
import enum

class Frequency(enum.Enum):
    daily = 'daily'
    monthly = 'monthly'
    yearly = 'yearly'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    frequency = db.Column(db.Enum(Frequency), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'frequency': self.frequency.value  # Utilise la valeur correcte
        }
