from .player import create_player
from .question import load_questions
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    load_questions("questions.json")
