from .player import create_player
from .question import load_questions
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_player("Alice")
    create_player("Bob")
    create_player("Chad")
    load_questions("questions.json")
